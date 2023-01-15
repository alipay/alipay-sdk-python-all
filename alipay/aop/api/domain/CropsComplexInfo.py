#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CropsGrowthInfo import CropsGrowthInfo
from alipay.aop.api.domain.CropsHarvestForecastInfo import CropsHarvestForecastInfo
from alipay.aop.api.domain.CropsHarvestProgressInfo import CropsHarvestProgressInfo
from alipay.aop.api.domain.CropsPlantingInfo import CropsPlantingInfo
from alipay.aop.api.domain.CropsSoilMoistureInfo import CropsSoilMoistureInfo
from alipay.aop.api.domain.AgWeatherDisasterInfo import AgWeatherDisasterInfo
from alipay.aop.api.domain.AgWeatherForecastInfo import AgWeatherForecastInfo
from alipay.aop.api.domain.CropsYieldForecastInfo import CropsYieldForecastInfo


class CropsComplexInfo(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.crops:
            if isinstance(self.crops, list):
                for i in range(0, len(self.crops)):
                    element = self.crops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crops[i] = element.to_alipay_dict()
            if hasattr(self.crops, 'to_alipay_dict'):
                params['crops'] = self.crops.to_alipay_dict()
            else:
                params['crops'] = self.crops
        if self.growth_info:
            if isinstance(self.growth_info, list):
                for i in range(0, len(self.growth_info)):
                    element = self.growth_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.growth_info[i] = element.to_alipay_dict()
            if hasattr(self.growth_info, 'to_alipay_dict'):
                params['growth_info'] = self.growth_info.to_alipay_dict()
            else:
                params['growth_info'] = self.growth_info
        if self.harvest_forecast_info:
            if isinstance(self.harvest_forecast_info, list):
                for i in range(0, len(self.harvest_forecast_info)):
                    element = self.harvest_forecast_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.harvest_forecast_info[i] = element.to_alipay_dict()
            if hasattr(self.harvest_forecast_info, 'to_alipay_dict'):
                params['harvest_forecast_info'] = self.harvest_forecast_info.to_alipay_dict()
            else:
                params['harvest_forecast_info'] = self.harvest_forecast_info
        if self.harvest_progress_info:
            if isinstance(self.harvest_progress_info, list):
                for i in range(0, len(self.harvest_progress_info)):
                    element = self.harvest_progress_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.harvest_progress_info[i] = element.to_alipay_dict()
            if hasattr(self.harvest_progress_info, 'to_alipay_dict'):
                params['harvest_progress_info'] = self.harvest_progress_info.to_alipay_dict()
            else:
                params['harvest_progress_info'] = self.harvest_progress_info
        if self.planting_info:
            if isinstance(self.planting_info, list):
                for i in range(0, len(self.planting_info)):
                    element = self.planting_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.planting_info[i] = element.to_alipay_dict()
            if hasattr(self.planting_info, 'to_alipay_dict'):
                params['planting_info'] = self.planting_info.to_alipay_dict()
            else:
                params['planting_info'] = self.planting_info
        if self.plot_area:
            if hasattr(self.plot_area, 'to_alipay_dict'):
                params['plot_area'] = self.plot_area.to_alipay_dict()
            else:
                params['plot_area'] = self.plot_area
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.soil_moisture_info:
            if isinstance(self.soil_moisture_info, list):
                for i in range(0, len(self.soil_moisture_info)):
                    element = self.soil_moisture_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.soil_moisture_info[i] = element.to_alipay_dict()
            if hasattr(self.soil_moisture_info, 'to_alipay_dict'):
                params['soil_moisture_info'] = self.soil_moisture_info.to_alipay_dict()
            else:
                params['soil_moisture_info'] = self.soil_moisture_info
        if self.update_date:
            if hasattr(self.update_date, 'to_alipay_dict'):
                params['update_date'] = self.update_date.to_alipay_dict()
            else:
                params['update_date'] = self.update_date
        if self.weather_disaster_info:
            if hasattr(self.weather_disaster_info, 'to_alipay_dict'):
                params['weather_disaster_info'] = self.weather_disaster_info.to_alipay_dict()
            else:
                params['weather_disaster_info'] = self.weather_disaster_info
        if self.weather_forecast_info:
            if hasattr(self.weather_forecast_info, 'to_alipay_dict'):
                params['weather_forecast_info'] = self.weather_forecast_info.to_alipay_dict()
            else:
                params['weather_forecast_info'] = self.weather_forecast_info
        if self.yield_forecast_info:
            if isinstance(self.yield_forecast_info, list):
                for i in range(0, len(self.yield_forecast_info)):
                    element = self.yield_forecast_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.yield_forecast_info[i] = element.to_alipay_dict()
            if hasattr(self.yield_forecast_info, 'to_alipay_dict'):
                params['yield_forecast_info'] = self.yield_forecast_info.to_alipay_dict()
            else:
                params['yield_forecast_info'] = self.yield_forecast_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsComplexInfo()
        if 'crops' in d:
            o.crops = d['crops']
        if 'growth_info' in d:
            o.growth_info = d['growth_info']
        if 'harvest_forecast_info' in d:
            o.harvest_forecast_info = d['harvest_forecast_info']
        if 'harvest_progress_info' in d:
            o.harvest_progress_info = d['harvest_progress_info']
        if 'planting_info' in d:
            o.planting_info = d['planting_info']
        if 'plot_area' in d:
            o.plot_area = d['plot_area']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'soil_moisture_info' in d:
            o.soil_moisture_info = d['soil_moisture_info']
        if 'update_date' in d:
            o.update_date = d['update_date']
        if 'weather_disaster_info' in d:
            o.weather_disaster_info = d['weather_disaster_info']
        if 'weather_forecast_info' in d:
            o.weather_forecast_info = d['weather_forecast_info']
        if 'yield_forecast_info' in d:
            o.yield_forecast_info = d['yield_forecast_info']
        return o


