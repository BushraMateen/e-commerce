import React from 'react';
import './ProductRow'

 class ProductRow extends React.Component {
    render() {
      const product = this.props.product;
      const title = product.title; 
      const image = product.image;  
      const description = product.description;
      const price = product.price;
      const rate = product.rate;
      const count = product.count;
  
      return (
       
        <div className="card">
         <img src={image} alt="Girl in a jacket" width="100%" />
          <p>{description}</p>
          <div className="container">
            <p>{title}</p>
            <p>{price}</p>
            <p>{rate}</p>
            <p>{count}</p>

          </div>
        </div>
  
      );
    }
  }

export default ProductRow