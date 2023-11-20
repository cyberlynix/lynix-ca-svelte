<script>
	import FlightBox from '$lib/components/flight/FlightBox.svelte';
</script>

<div class="header" style="position:relative;">
	<img
		src="https://www.thetimes.co.uk/travel/wp-content/uploads/sites/6/2021/06/Toronto-Ontario-Canada_Credit_GettyImages-1001151076-1.jpg?w=2200&h=880&crop=1"
		alt="Lynix's Fursona Refsheet made by Maxwell_Wolf"
	/>
	<div class="header-content">
		<div>
			<h1>Furnal Equinox 2024: Under the Sea</h1>
			<br />
			<p>March 15th 2024 - March 17th 2024 <span class="badge">Going (Confirmed)</span></p>
		</div>
	</div>
</div>

<!-- Navigation -->
<div>
    <div class="nav-container">
        <div class="nav">
            <a class="active" href="/events/furnal-equinox-2024">Overview</a>
            <a href="/events/furnal-equinox-2024/itinerary">Itinerary</a>
            <a href="/events/furnal-equinox-2024/meetups">Meetups</a>
            <a href="/events/furnal-equinox-2024/panels">Live Location and Panels</a>
            <a href="/events/furnal-equinox-2024/gallery">Gallery</a>
        </div>
    </div>
</div>

<div style="padding: 5em;">
    <div class="">
        <h1 style="color:#fff;margin-bottom:2rem;">Flight Details</h1>
    </div>
    <p >Arrival Flight: <span class='font-bold'>AC 647 ({'YQM -> YYZ'})</span></p>
    <p style='margin-bottom:2rem;'>Departure Flight: <span class='font-bold'>AC 648 ({'YYZ -> YQM'})</span></p>
    <br/>
	<div class="width:600px;" style="margin-bottom:2rem;">
		<FlightBox />
	</div>
    <div class="">
        <h1 style="color:#fff;margin-bottom:1rem;">Weather Information</h1>
        <p>No cities are configured on Openweather API!</p>
    </div>
    <div class="">
        <h1 style="color:#fff;margin-bottom:1rem;margin-top:2rem;">Event Pre-Checklist</h1>
        <p>Unavailable at this time.</p>
    </div>
</div>

<style>
    .nav-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        background: #1d1f20;
        padding: 1rem 0;
    }

    .nav {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 3rem;
    }

    .nav a {
        color: #fff;
        font-weight: 600;
        font-size: 1.2rem;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .nav a:hover {
        color: #0ea5e9;
    }

    .nav a.active {
        all: unset;
        font-weight: 600;
        font-size: 1.2rem;
        color: #0ea5e9;
    }

	.header {
		position: inherit;
		height: 600px;
	}

	.header img {
		width: 100%;
		height: 600px;
		object-fit: cover;
		object-position: center;
	}

	.header-content {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.7);
		display: flex;
		flex-direction: column;
		justify-content: center;
		padding: 2em 5em;
		color: white;
	}

	.header-content h1 {
		font-size: 50px;
		font-weight: 700;
	}

	.header-content p {
		font-weight: 500;
		font-size: 20px;
	}

	.badge {
		margin-left: 0.7em;
		border-radius: 99999px;
		background-color: #22c55e;
		color: black;
		font-weight: 600;
		padding: 0.3em 0.7em;
	}
</style>
