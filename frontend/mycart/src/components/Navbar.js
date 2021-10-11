import { Button, Container, Divider, Grid, Header, Image, Menu, Segment } from 'semantic-ui-react'


function Navbar() {
    return(<Grid>
        <Grid.Column>
        <Menu
          items={[
            { key: '1', name: 'link-1', content: 'Link' },
            { key: '2', name: 'link-2', content: 'Link' },
            { key: '3', name: 'link-3', content: 'Link' },
          ]}
          pointing
          secondary
        />
      </Grid.Column>
    </Grid>)
}

export default Navbar;