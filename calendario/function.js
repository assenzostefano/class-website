var checkbox = document.querySelector('input[name=mode]');

        checkbox.addEventListener('change', function() {
            if(this.checked) {
                trans()
                document.documentElement.setAttribute('data-theme', 'dartheme')
            } else {
                trans()
                document.documentElement.setAttribute('data-theme', 'lighttheme')
            }
        })

        let trans = () => {
            document.documentElement.classList.add('transition');
            window.setTimeout(() => {
                document.documentElement.classList.remove('transition');
            }, 1000)
        }

        const btn = document.querySelector(".container_toggle");

        const currentTheme = localStorage.getItem("theme");
        if (currentTheme == "dark") {
          document.body.classList.add("dark-theme");
        }
        
        btn.addEventListener("click", function () {
          document.body.classList.toggle("dark-theme");
        
          let theme = "light";
          if (document.body.classList.contains("dark-theme")) {
            theme = "dark";
          }
          localStorage.setItem("theme", theme);
        });
