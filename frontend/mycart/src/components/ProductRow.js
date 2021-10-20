import React from 'react';
import './ProductRow'
import './ProductRow.css'

 class ProductRow extends React.Component {
    render() {
      const product = this.props.product;
      const Categroy = product.Categroy; 
      const title = product.title; 
      const image = product.image;  
      const description = product.description;
      const price = product.price;
      
      
  
      return (
       
        // <div className="card">
        //  <img src={image} alt="Girl in a jacket" width="75%" />
         
        //   <div className="container"> 
        //     <p>{title}</p>
        //     <p>{description}</p>
        //     <p>{price}</p>
           
        //    </div>
        // </div>  
        
        <div className="card_layout" >
          <div className="card_header">
            <h2>{Categroy}</h2>
          </div>
          <div className="card_body">
            <img src={image} alt="Girl in a jacket" width="25%" />
          </div>
          <div className="card_footer">
            <p><strong>Tittle : </strong> {title}</p>
            <p><strong>Description: </strong>{description}</p>
            <p><strong>Price: </strong>{price}</p>
          </div>
        </div>
  
      );
    }
  }

export default ProductRow