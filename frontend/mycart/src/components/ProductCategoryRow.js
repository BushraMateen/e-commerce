import React from 'react';
import './ProductCategoryRow'
import './ProductCategoryRow.css'



class ProductCategoryRow extends React.Component {
    render() {
      const category = this.props.category;
      return (
        <div className="product_container">
        <tr>
          <th colSpan="2">
            {category}
          </th>
        </tr>
        </div>
      );
    }
  }


  export default ProductCategoryRow