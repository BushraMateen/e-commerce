import React from "react";
import SearchIcon from '@material-ui/icons/Search'

function Header() {
    return(
        <nav className="header">
            <div className="header__search">
                <input type="text" className="header_search" />
                <SearchIcon className="header__searxhIcon" />
            </div>
            <div className="header__option">
                <span className="header__optionone">login</span>
            </div>

        </nav>
    )
}


export default Header