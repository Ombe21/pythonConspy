<script>
    import {Route, Router, Link} from "svelte-routing";
    import Admin from "./Admin.svelte"
    import Home from "./Home.svelte"

    export let url = "";
</script>

<Router url="{url}">
  <nav>
    <Link to="/">Home</Link>
    <Link to="admin">Admin</Link>
  </nav>
  <div>
    <Route path="admin" component="{Admin}" />
    <Route path="/"><Home /></Route>
  </div>
</Router>