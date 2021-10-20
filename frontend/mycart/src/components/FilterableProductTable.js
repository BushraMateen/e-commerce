import React from 'react';
import ProductTable from './ProductTable'
import './FilterableProductTable.css'

class FilterableProductTable extends React.Component {
    render() {
        return (
            <div className="grid-container">
              <ProductTable products={this.props.product} />
            </div>
          );
        }
      }

      export default FilterableProductTable