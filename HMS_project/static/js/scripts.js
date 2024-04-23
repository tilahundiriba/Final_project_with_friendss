const sidebarToggle = document.querySelector("#sidebar-toggle");
sidebarToggle.addEventListener("click",function(){
    document.querySelector("#sidebar").classList.toggle("collapsed");
});

document.querySelector(".theme-toggle").addEventListener("click",() => {
    toggleLocalStorage();
    toggleRootClass();
});

function toggleRootClass(){
    const current = document.documentElement.getAttribute('data-bs-theme');
    const inverted = current == 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-bs-theme',inverted);
}

function toggleLocalStorage(){
    if(isLight()){
        localStorage.removeItem("light");
    }else{
        localStorage.setItem("light","set");
    }
}

function isLight(){
    return localStorage.getItem("light");
}

if(isLight()){
    toggleRootClass();
}
function googleTranslateElementInit() {
    new google.translate.TranslateElement(
      { pageLanguage: 'en', defaultLanguage: 'en' },
      'google_translate_element'
    );
  }

		// JavaScript code for pagination
		document.addEventListener('DOMContentLoaded', function () {
			// Get the table rows and calculate total pages
			var tableRows = document.querySelectorAll('#tableId tbody tr');
			var totalPages = Math.ceil(tableRows.length / 5);

			// Generate pagination links
			var paginationContainer = document.querySelector('.pagination');
			for (var i = 1; i <= totalPages; i++) {
				var pageLink = document.createElement('a');
				pageLink.href = '#';
				pageLink.textContent = i;
				pageLink.addEventListener('click', function (event) {
					event.preventDefault();
					showPage(parseInt(this.textContent));
				});
				paginationContainer.appendChild(pageLink);
			}

			// Function to show page
			function showPage(pageNumber) {
				// Hide all table rows
				tableRows.forEach(function (row) {
					row.style.display = 'none';
				});

				// Calculate start and end indexes for current page
				var startIndex = (pageNumber - 1) * 5;
				var endIndex = startIndex + 5;

				// Show table rows for current page
				for (var i = startIndex; i < endIndex && i < tableRows.length; i++) {
					tableRows[i].style.display = '';
				}
			}

			// Show the first page by default
			showPage(1);
		});
