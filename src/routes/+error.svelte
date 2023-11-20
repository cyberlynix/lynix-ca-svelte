<script>
    // @ts-nocheck

	import { page } from '$app/stores';
</script>

<div>
    <h1><span style="font-size:80px;color:#22c55e;">{$page.status}</span><br/> <span style="color:#06b6d4;">{$page.error.message}</span></h1>
    <p style="margin-top:1rem;font-size:18px;font-weight:500;text-align:center;">
        {#if $page.status === 404} 
            The resource or page you were looking for could not be found. <br/><br/>
            <a href="/">Return to the homepage</a>
        {/if}</p>
</div>


<style>
    div {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    h1 {
        text-align: center;
    }
</style>