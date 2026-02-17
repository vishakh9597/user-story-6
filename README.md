# user-story-6User Story: Build an Insightful and Visually Rich Power BI Dashboard with Book Subcategory Analytics
As a data analyst,
I want to build a highly interactive and visually engaging Power BI dashboard using the scraped book data,
So that stakeholders can easily explore trends, outliers, and key insights across book categories and subcategories like Travel, Music, Science, and more.

Acceptance Criteria
Data Modeling & Integration
Extend the dataset to include book subcategories (e.g., Travel, Music, Fiction, Non-Fiction, Science, etc.) by scraping them from category links or deriving them from the product URLs.

Convert all price values from GBP (£) to USD ($) using a fixed or real-time exchange rate (e.g., £1 = $1.32).
Implement book tier classification based on USD price:
Budget: under $26.40 (~£20)
Standard: $26.40 – $66.00 (~£20–£50)
Premium: over $66.00 (~£50)

Clean and transform data in Power Query Editor, ensuring consistency across fields.
Enforce appropriate data types:
Price → Decimal
Rating → Whole Number
Availability → Text
Subcategory → Text
Advanced Visualizations with Subcategory Focus
Visuals to Include
Category & Subcategory Tree Map
Display book count and average price per subcategory.
Use conditional color formatting based on average rating or in-stock percentage.
Decomposition Tree (Drill-through Enabled)
Analyze data from: Category → Subcategory → Rating → Availability → Price Tier.
Allow users to interactively explore outliers and distribution patterns (e.g., “Music > Rating 5 > Out of Stock”).
Multi-Row Cards or KPI Grid
Show dynamic KPIs like:
Highest-rated book (per subcategory)
Average price
% In stock
Total books
Update dynamically via slicers and filters.
Stacked Column Chart
Display availability status (In Stock / Out of Stock) per subcategory.
Scatter Plot with Trend Line
Plot Price vs. Rating, colored by Subcategory.
Add a regression trend line to visualize correlations.
Smart Narrative & Key Insights
Auto-generate natural language summaries like:
"The Travel subcategory has the highest average price at $55.25, but 40% of titles are currently out of stock."
Bookmarks & Page Navigation
Use custom bookmark buttons to toggle between:
Overview
Pricing Analysis
Availability Trends
Subcategory Deep-Dive
Slicers / Filters
Include interactive slicers for:
Subcategory
Rating
Price Tier
Availability

**At the end write each individual comments of what was your observation on this and "KEY FINDINGS FROM THIS VISUALIZATION".
