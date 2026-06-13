function capitalize(str){
    return str.charAt(0).toUpperCase() + str.slice(1);
}

document.addEventListener("DOMContentLoaded", () => {

    const currentDirection = document.querySelector(".main").getAttribute("data-direction");
    const from = document.getElementById("unit-from");
    const to = document.getElementById("unit-to");
    const swap_btn = document.getElementById("swap-btn");

    const units_from_url = currentDirection.split('-');
    const unit1 = units_from_url[0];
    const unit2 = units_from_url[2];

    if (currentDirection === `${unit1}-to-${unit2}`){
        from.innerText = capitalize(unit1);
        to.innerText = capitalize(unit2);
    }

    if (swap_btn){
        document.getElementById("swap-btn").addEventListener("click", () =>{

            if (currentDirection === `${unit1}-to-${unit2}`){
                window.location.href = `/${unit1}-${unit2}/${unit2}-to-${unit1}`;

            } else{
                window.location.href = `/${unit2}-${unit1}/${unit1}-to-${unit2}`;
            }
        });
    }

});