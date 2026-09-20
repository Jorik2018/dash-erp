pipeline {
    agent any

    environment {
        SERVICE_ID = 'dash-erp'
        DEPLOY_DIR = 'D:\\apps\\dash-erp'
        PORT = '7781'
        BASE_PATH = 'dash'
    }

    stages {

        // ============================================================
        // 1. Verificar entorno
        // ============================================================

        stage('Check Environment') {
            steps {
                bat '''
                    SET PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%

                    echo ==============================
                    echo PYTHON
                    echo ==============================

                    python --version
                    python -m pip --version

                    echo ==============================
                    echo GIT
                    echo ==============================

                    git --version
                '''
            }
        }


        // ============================================================
        // 2. Detener servicio anterior
        // ============================================================

        stage('Stop Service') {
            steps {
                bat '''
                    "%PYTHON_HOME%\\python.exe" ^
                        "%SERVICE_MANAGER%" ^
                        stop ^
                        "%SERVICE_ID%"
                '''
            }
        }


        // ============================================================
        // 3. Copiar aplicación
        // ============================================================

        stage('Deploy Files') {
            steps {
                powershell '''
                    $source = $env:WORKSPACE
                    $destination = $env:DEPLOY_DIR

                    if (-not (Test-Path $destination)) {
                        New-Item `
                            -ItemType Directory `
                            -Path $destination `
                            -Force | Out-Null
                    }

                    robocopy `
                        $source `
                        $destination `
                        /MIR `
                        /XD ".git" ".venv" "__pycache__" ".pytest_cache" `
                        /XF ".env" "*.pyc"

                    $code = $LASTEXITCODE

                    # Robocopy 0-7 = OK
                    if ($code -gt 7) {
                        throw "Robocopy failed with exit code $code"
                    }

                    exit 0
                '''
            }
        }


        // ============================================================
        // 4. Crear entorno Python de producción
        // ============================================================

        stage('Prepare Python Environment') {
            steps {
                bat '''
                    if not exist "%DEPLOY_DIR%\\.venv" (
                        "%PYTHON_HOME%\\python.exe" ^
                            -m venv ^
                            "%DEPLOY_DIR%\\.venv"
                    )

                    "%DEPLOY_DIR%\\.venv\\Scripts\\python.exe" ^
                        -m pip install ^
                        --upgrade pip
                '''
            }
        }


        // ============================================================
        // 5. Instalar Poetry
        // ============================================================

        stage('Install Poetry') {
            steps {
                bat '''
                    "%DEPLOY_DIR%\\.venv\\Scripts\\python.exe" ^
                        -m pip install ^
                        poetry
                '''
            }
        }


        // ============================================================
        // 6. Instalar dependencias
        // ============================================================

        stage('Install Dependencies') {
            steps {
                bat '''
                    cd /D "%DEPLOY_DIR%"

                    SET POETRY_VIRTUALENVS_CREATE=false

                    "%DEPLOY_DIR%\\.venv\\Scripts\\poetry.exe" ^
                        install ^
                        --only main ^
                        --no-interaction ^
                        --no-ansi
                '''
            }
        }


        // ============================================================
        // 7. Verificar Dash + Waitress
        // ============================================================

        stage('Verify Application') {
            steps {
                bat '''
                    cd /D "%DEPLOY_DIR%"

                    echo ==============================
                    echo DASH
                    echo ==============================

                    "%DEPLOY_DIR%\\.venv\\Scripts\\python.exe" ^
                        -c "import dash; print('Dash:', dash.__version__)"

                    echo ==============================
                    echo WAITRESS
                    echo ==============================

                    "%DEPLOY_DIR%\\.venv\\Scripts\\waitress-serve.exe" ^
                        --help > nul

                    echo Waitress OK
                '''
            }
        }


        // ============================================================
        // 8. Configurar servicio Windows
        // ============================================================

stage('Configure Service') {
    steps {
        withCredentials([
            string(
                credentialsId: 'VAULT_TOKEN',
                variable: 'VAULT_TOKEN'
            )
        ]) {
            bat '''
                echo ==========================================
                echo Configuring Dash Windows service
                echo ==========================================

                "%PYTHON_HOME%\\python.exe" "%SERVICE_MANAGER%" install ^
                    "%SERVICE_ID%" ^
                    "%DEPLOY_DIR%" ^
                    --name "Dash ERP" ^
                    --description "Dash ERP Application" ^
                    --type waitress ^
                    --main "dash_erp.app:server" ^
                    --host "127.0.0.1:%PORT%" ^
                    --env "VAULT_ADDR=%VAULT_ADDR%" ^
                    --env "VAULT_TOKEN=%VAULT_TOKEN%"

                if errorlevel 1 (
                    echo ERROR: Service configuration failed
                    exit /B 1
                )
            '''
        }
    }
}

        // ============================================================
        // 9. Arrancar servicio
        // ============================================================

        stage('Start Service') {
            steps {
                bat '''
                    "%PYTHON_HOME%\\python.exe" ^
                        "%SERVICE_MANAGER%" ^
                        start ^
                        "%SERVICE_ID%"
                '''
            }
        }


        // ============================================================
        // 10. Verificar servicio
        // ============================================================

        stage('Verify Service') {
            steps {
                bat '''
                    "%PYTHON_HOME%\\python.exe" ^
                        "%SERVICE_MANAGER%" ^
                        status ^
                        "%SERVICE_ID%"
                '''
            }
        }


        // ============================================================
        // 11. Health Check
        // ============================================================

        stage('Health Check') {
            steps {
                powershell '''
                    $url = "http://127.0.0.1:$env:PORT/$env:BASE_PATH/"

                    $maxAttempts = 10

                    for ($attempt = 1; $attempt -le $maxAttempts; $attempt++) {

                        Write-Host "Health check $attempt/$maxAttempts"
                        Write-Host $url

                        try {

                            $response = Invoke-WebRequest `
                                -UseBasicParsing `
                                -Uri $url `
                                -TimeoutSec 5

                            if ($response.StatusCode -eq 200) {

                                Write-Host "Dash ERP OK"

                                exit 0
                            }

                        }
                        catch {

                            Write-Host "Dash aun no disponible."
                        }

                        Start-Sleep -Seconds 3
                    }

                    throw "Dash ERP no respondio al health check."
                '''
            }
        }
    }

    post {
        success {
            echo 'Dash ERP desplegado correctamente.'
            echo 'URL interna: http://127.0.0.1:%PORT%/dash/'
        }
        failure {
            echo 'Fallo desplegando Dash ERP.'
        }
    }
}