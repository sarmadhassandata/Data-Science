$renameMap = [ordered]@{
    # 1. Datetime Indexing & Visualization
    "Manipulating Time Series Data in Python.ipynb"                      = "01_Time_Series_Data_Manipulation_and_Indexing.ipynb"
    "Visualizing Time Series Data in Python.ipynb"                         = "02_Time_Series_Data_Visualization.ipynb"

    # 2. Statistical Analysis, Decomposition & Stationarity
    "Introduction to Forecasting and Time Series Analysis in Python.ipynb" = "03_Introduction_to_Time_Series_Analysis_and_Forecasting.ipynb"
    "Time Series Analysis in Python.ipynb"                                = "04_Statistical_Time_Series_Analysis_and_Stationarity.ipynb"
    "Time Series Analysis.ipynb"                                           = "05_Time_Series_Decomposition_and_Trend_Analysis.ipynb"

    # 3. Classical Statistical Forecasting (ARIMA/SARIMAX)
    "ARIMA Models in Python.ipynb"                                         = "06_ARIMA_and_SARIMAX_Statistical_Forecasting.ipynb"
    "Time Series Forecasting.ipynb"                                        = "07_Time_Series_Forecasting_Methods_and_Validation.ipynb"

    # 4. Machine Learning & Domain Case Studies
    "Machine Learning for Time Series Data in Python.ipynb"                = "08_Machine_Learning_for_Time_Series_Forecasting.ipynb"
    "43_Timeline Analysis (Covid-19).ipynb"                                = "09_Covid19_Epidemiological_Timeline_Analysis_Case_Study.ipynb"
}

# Fallback pattern matching for truncated filenames if exact path isn't found
foreach ($file in Get-ChildItem -Filter "*.ipynb") {
    $matched = $false
    foreach ($oldKey in $renameMap.Keys) {
        $shortKey = $oldKey.Substring(0, [System.Math]::Min(25, $oldKey.Length))
        if ($file.Name -eq $oldKey -or $file.Name.StartsWith($shortKey)) {
            Rename-Item -Path $file.FullName -NewName $renameMap[$oldKey]
            Write-Host "RENAMED: $($file.Name) -> $($renameMap[$oldKey])" -ForegroundColor Green
            $matched = $true
            break
        }
    }
    if (-not $matched -and $file.Name -notmatch "^\d{2}_") {
        Write-Host "SKIPPED: $($file.Name)" -ForegroundColor Yellow
    }
}
