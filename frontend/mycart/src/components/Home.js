import React, { useState, useEffect} from 'react';
import './Home.css'

function Home(){
    
const [products, setProducts] = useState([]);

useEffect(()=> {
    // fetch('http://127.0.0.1:8000/product')
    fetch("https://fakestoreapi.com/products")
    .then(reponse => reponse.json())
    .then(data => {
        setProducts(data);
    });
}, []);



return(
    <div id="homecontainer">
        {products.map(p => 
                <div className="productList">
                  
                    <li>{p.id}</li>
                    <li>{p.title}</li>
                    <li>{p.price}</li>
                    <li>{p.description}</li>
                    <li>{p.category}</li>
                    <div className="home__image">
                    <img 
                    src={p.image}
                    alt="" />
                    </div>
                </div>)}
    </div>
)
}


 export default Home