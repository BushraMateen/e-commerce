import React from 'react';
import ProductTable from './ProductTable'


class FilterableProductTable extends React.Component {
    render() {
        return (
            <div>
              
              <ProductTable products={this.props.product} />
            </div>
          );
        }
      }

      export default FilterableProductTable