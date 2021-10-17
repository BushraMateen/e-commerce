
import React from 'react';
import ProductCategoryRow from './ProductCategoryRow'
import ProductRow from './ProductRow'
import './ProductTable'


 class ProductTable extends React.Component {
    render() {
      const rows = [];
      let lastCategory = null;
      
      this.props.products.forEach((product) => {
        if (product.category !== lastCategory) {
          rows.push(
            <ProductCategoryRow
              category={product.category}
              key={product.category} />
          );
        }
        rows.push(
          <ProductRow
            product={product}
            key={product.title} />
        );
        lastCategory = product.category;
      });
  
      return (
        <div className="card-container">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Price</th>
           
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
          </div>
      );
    }
  }

  export default ProductTable