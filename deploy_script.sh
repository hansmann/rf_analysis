#!/bin/bash

# Script to deploy the Illinois school districts analysis to GitHub Pages

echo "Deploying Illinois School Districts Analysis to GitHub Pages..."

# Navigate to your project directory (adjust path if needed)
cd /Users/willhansmann/code/teachers

# Copy the chart file to index.html to make it the main page
cp final_accurate_chart.html index.html

# Initialize git if not already done
if [ ! -d ".git" ]; then
    git init
    git remote add origin https://github.com/hansmann/rf_analysis.git
fi

# Add all files
git add .

# Commit with descriptive message
git commit -m "Add Illinois school districts income vs teacher salary analysis

- Interactive chart with 25+ districts
- Real data from US Census 2023 and Illinois ISBE
- Shows correlation between community wealth and teacher compensation
- Highlights River Forest SD 90 in analysis"

# Push to GitHub
git push -u origin main

echo ""
echo "Deployment complete!"
echo ""
echo "Your chart will be available at:"
echo "https://hansmann.github.io/rf_analysis/"
echo ""
echo "Note: GitHub Pages may take a few minutes to deploy."
echo "You'll need to enable GitHub Pages in your repository settings if not already done:"
echo "Go to: https://github.com/hansmann/rf_analysis/settings/pages"
echo "Select 'Deploy from a branch' and choose 'main' branch"