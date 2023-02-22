#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CropsGrowthInfo import CropsGrowthInfo
from alipay.aop.api.domain.CropsHarvestForecastInfo import CropsHarvestForecastInfo
from alipay.aop.api.domain.CropsHarvestProgressInfo import CropsHarvestProgressInfo
from alipay.aop.api.domain.CropsPlantingInfo import CropsPlantingInfo
from alipay.aop.api.domain.CropsSoilMoistureInfo import CropsSoilMoistureInfo
from alipay.aop.api.domain.AgWeatherDisasterInfo import AgWeatherDisasterInfo
from alipay.aop.api.domain.AgWeatherForecastInfo import AgWeatherForecastInfo
from alipay.aop.api.domain.CropsYieldForecastInfo import CropsYieldForecastInfo


class AnttechBlockchainDefinDataserviceCropbaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceCropbaseQueryResponse, self).__init__()
        self._crops = None
        self._growth_info = None
        self._harvest_forecast_info = None
        self._harvest_progress_info = None
        self._planting_info = None
        self._plot_area = None
        self._region_code = None
        self._soil_moisture_info = None
        self._update_date = None
        self._weather_disaster_info = None
        self._weather_forecast_info = None
        self._yield_forecast_info = None

    @property
    def crops(self):
        return self._crops

    @crops.setter
    def crops(self, value):
        if isinstance(value, list):
            self._crops = list()
            for i in value:
                self._crops.append(i)
    @property
    def growth_info(self):
        return self._growth_info

    @growth_info.setter
    def growth_info(self, value):
        if isinstance(value, list):
            self._growth_info = list()
            for i in value:
                if isinstance(i, CropsGrowthInfo):
                    self._growth_info.append(i)
                else:
                    self._growth_info.append(CropsGrowthInfo.from_alipay_dict(i))
    @property
    def harvest_forecast_info(self):
        return self._harvest_forecast_info

    @harvest_forecast_info.setter
    def harvest_forecast_info(self, value):
        if isinstance(value, list):
            self._harvest_forecast_info = list()
            for i in value:
                if isinstance(i, CropsHarvestForecastInfo):
                    self._harvest_forecast_info.append(i)
                else:
                    self._harvest_forecast_info.append(CropsHarvestForecastInfo.from_alipay_dict(i))
    @property
    def harvest_progress_info(self):
        return self._harvest_progress_info

    @harvest_progress_info.setter
    def harvest_progress_info(self, value):
        if isinstance(value, list):
            self._harvest_progress_info = list()
            for i in value:
                if isinstance(i, CropsHarvestProgressInfo):
                    self._harvest_progress_info.append(i)
                else:
                    self._harvest_progress_info.append(CropsHarvestProgressInfo.from_alipay_dict(i))
    @property
    def planting_info(self):
        return self._planting_info

    @planting_info.setter
    def planting_info(self, value):
        if isinstance(value, list):
            self._planting_info = list()
            for i in value:
                if isinstance(i, CropsPlantingInfo):
                    self._planting_info.append(i)
                else:
                    self._planting_info.append(CropsPlantingInfo.from_alipay_dict(i))
    @property
    def plot_area(self):
        return self._plot_area

    @plot_area.setter
    def plot_area(self, value):
        self._plot_area = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def soil_moisture_info(self):
        return self._soil_moisture_info

    @soil_moisture_info.setter
    def soil_moisture_info(self, value):
        if isinstance(value, list):
            self._soil_moisture_info = list()
            for i in value:
                if isinstance(i, CropsSoilMoistureInfo):
                    self._soil_moisture_info.append(i)
                else:
                    self._soil_moisture_info.append(CropsSoilMoistureInfo.from_alipay_dict(i))
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value
    @property
    def weather_disaster_info(self):
        return self._weather_disaster_info

    @weather_disaster_info.setter
    def weather_disaster_info(self, value):
        if isinstance(value, AgWeatherDisasterInfo):
            self._weather_disaster_info = value
        else:
            self._weather_disaster_info = AgWeatherDisasterInfo.from_alipay_dict(value)
    @property
    def weather_forecast_info(self):
        return self._weather_forecast_info

    @weather_forecast_info.setter
    def weather_forecast_info(self, value):
        if isinstance(value, AgWeatherForecastInfo):
            self._weather_forecast_info = value
        else:
            self._weather_forecast_info = AgWeatherForecastInfo.from_alipay_dict(value)
    @property
    def yield_forecast_info(self):
        return self._yield_forecast_info

    @yield_forecast_info.setter
    def yield_forecast_info(self, value):
        if isinstance(value, list):
            self._yield_forecast_info = list()
            for i in value:
                if isinstance(i, CropsYieldForecastInfo):
                    self._yield_forecast_info.append(i)
                else:
                    self._yield_forecast_info.append(CropsYieldForecastInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceCropbaseQueryResponse, self).parse_response_content(response_content)
        if 'crops' in response:
            self.crops = response['crops']
        if 'growth_info' in response:
            self.growth_info = response['growth_info']
        if 'harvest_forecast_info' in response:
            self.harvest_forecast_info = response['harvest_forecast_info']
        if 'harvest_progress_info' in response:
            self.harvest_progress_info = response['harvest_progress_info']
        if 'planting_info' in response:
            self.planting_info = response['planting_info']
        if 'plot_area' in response:
            self.plot_area = response['plot_area']
        if 'region_code' in response:
            self.region_code = response['region_code']
        if 'soil_moisture_info' in response:
            self.soil_moisture_info = response['soil_moisture_info']
        if 'update_date' in response:
            self.update_date = response['update_date']
        if 'weather_disaster_info' in response:
            self.weather_disaster_info = response['weather_disaster_info']
        if 'weather_forecast_info' in response:
            self.weather_forecast_info = response['weather_forecast_info']
        if 'yield_forecast_info' in response:
            self.yield_forecast_info = response['yield_forecast_info']
