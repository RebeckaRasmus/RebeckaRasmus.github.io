---
layout: default
title: "Schema"
---

<div class="full-bleed">
  <section class="heroSchema">
    <div class="content">
      <h1>Rebecka &amp; Rasmus</h1>
      <h2>29 augusti 2026</h2>
      <div id="countdown"></div>
      <script src="/assets/script.js"></script>
      <br />
      <br />
    </div>
  </section>
</div>

<style>
  .wedding-schedule-wrapper {
    max-width: 600px;
    margin: 40px auto;
    padding: 0 20px;
  }

  .schedule-container {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .schedule-header {
    background: transparent;
    color: #333;
    padding: 30px 30px 20px 30px;
    text-align: center;
  }

  .schedule-header h1 {
    font-size: 2.5rem;
    font-weight: 300;
    margin-bottom: 10px;
    font-family: 'Playfair Display', serif;
  }

  .schedule-header p {
    font-size: 1.1rem;
    opacity: 0.7;
  }

  .schedule-content {
    padding: 0 30px 30px 30px;
  }

  .day-section {
    margin-bottom: 30px;
  }

  .day-section:last-child {
    margin-bottom: 0;
  }

  .day-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #f0f0f0;
    text-transform: capitalize;
  }

  .schedule-event {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
    padding: 15px;
    border-radius: 10px;
    transition: all 0.3s ease;
  }

  .schedule-event:hover {
    background: #f8f9ff;
    transform: translateX(5px);
  }

  .event-time {
    font-size: 1.1rem;
    font-weight: 600;
    color: #764ba2;
    min-width: 70px;
    padding-top: 2px;
  }

  .event-details {
    flex: 1;
    padding-left: 20px;
  }

  .event-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 5px;
  }

  .event-description {
    font-size: 0.95rem;
    color: #666;
    line-height: 1.4;
  }

  @media (max-width: 600px) {
    .wedding-schedule-wrapper {
      margin: 20px auto;
    }

    .schedule-header h1 {
      font-size: 2rem;
    }

    .schedule-header {
      padding: 20px 20px 15px 20px;
    }

    .schedule-content {
      padding: 0 20px 20px 20px;
    }

    .schedule-event {
      flex-direction: column;
    }

    .event-time {
      margin-bottom: 8px;
    }

    .event-details {
      padding-left: 0;
    }
  }
</style>

<div class="wedding-schedule-wrapper">
  <div class="schedule-container">
    <div class="schedule-header">
      <h1>Bröllopsprogram</h1>
      <p>Schema för helgen</p>
    </div>

    <div class="schedule-content">
      <div class="day-section">
        <div class="day-title">Fredag</div>

        <div class="schedule-event">
          <div class="event-time">20:00</div>
          <div class="event-details">
            <div class="event-title">Meet and greet</div>
            <div class="event-description">Alla som vill möts på Hotell Norra Vättern</div>
          </div>
        </div>
      </div>

      <div class="day-section">
        <div class="day-title">Lördag</div>

        <div class="schedule-event">
          <div class="event-time">15:00</div>
          <div class="event-details">
            <div class="event-title">Vigsel</div>
            <div class="event-description">Askersunds landskyrka</div>
          </div>
        </div>

        <div class="schedule-event">
          <div class="event-time">16:15</div>
          <div class="event-details">
            <div class="event-title">Transport</div>
            <div class="event-description">Buss till Stjernsunds slott för gäster</div>
          </div>
        </div>

        <div class="schedule-event">
          <div class="event-time">18:30</div>
          <div class="event-details">
            <div class="event-title">Bröllopsmiddag</div>
            <div class="event-description">Förrättning och middag</div>
          </div>
        </div>

        <div class="schedule-event">
          <div class="event-time">23:00</div>
          <div class="event-details">
            <div class="event-title">Transport</div>
            <div class="event-description">Första bussen till Hotell Norra Vättern </div>
          </div>
        </div>
      </div>

      <div class="day-section">
        <div class="day-title">Söndag</div>

        <div class="schedule-event">
          <div class="event-time">01:00</div>
          <div class="event-details">
            <div class="event-title">Transport</div>
            <div class="event-description">Andra bussen Hotell Norra Vättern</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
