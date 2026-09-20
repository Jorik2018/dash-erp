function initializeSidebarResize() {

    const sidebar =
        document.getElementById("sidebar");

    const resizer =
        document.getElementById("sidebar-resizer");

    const mainContent =
        document.getElementById("main-content");

    if (!sidebar || !resizer || !mainContent) {
        setTimeout(
            initializeSidebarResize,
            300
        );

        return;
    }


    if (resizer.dataset.initialized === "true") {
        return;
    }

    resizer.dataset.initialized = "true";


    let resizing = false;


    resizer.addEventListener(
        "mousedown",
        function () {

            if (
                sidebar.classList.contains(
                    "collapsed"
                )
            ) {
                return;
            }

            resizing = true;

            document.body.style.cursor =
                "ew-resize";

            document.body.style.userSelect =
                "none";
        }
    );


    document.addEventListener(
        "mousemove",
        function (event) {

            if (!resizing) {
                return;
            }


            let width = event.clientX;

            const minWidth = 150;
            const maxWidth = 420;


            width = Math.max(
                minWidth,
                Math.min(
                    maxWidth,
                    width
                )
            );


            document.documentElement
                .style
                .setProperty(
                    "--sidebar-width",
                    `${width}px`
                );
        }
    );


    document.addEventListener(
        "mouseup",
        function () {

            if (!resizing) {
                return;
            }

            resizing = false;

            document.body.style.cursor = "";
            document.body.style.userSelect = "";
        }
    );
}


initializeSidebarResize();