var activeQ = document.getElementById('q1');
var activeD = document.getElementById('d1');

function changeQuote(n) {
	activeQ.classList.remove("active");
	activeD.classList.remove("active");

	activeQ = document.getElementById(n);
	activeD = document.getElementById("d" + n.slice(-1));
	activeQ.className += " active";
	activeD.className += " active";
}