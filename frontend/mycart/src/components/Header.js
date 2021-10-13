import React from 'react';
import SearchIcon from '@mui/icons-material/Search'
import './Header.css'
import { Link } from 'react-router-dom'
import ShoppingBasketIcon from '@mui/icons-material/ShoppingBasket'

function Header() {
    return(
        <nav className="header">
            <div className="header__name">
                <span className="header1">Flikcart</span>
            </div>
            <div className="header__search">
                <input type="text" className="header__search" />
                <SearchIcon className="header__searchIcon" />
            </div>
            <Link to = "/login" className="header__link">
                <div className="header__option">
                    <span className="header__optionone">login</span>
                </div>
            </Link>
            <Link to="/checkout" className="Checkout__link">
                <div className="header__optionBasket">
                    <ShoppingBasketIcon />
                    <span className="header_optionline header__basketCount">2</span>
                </div>
            </Link>
        </nav>
    )
}


export default Header