#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CropsGrowthInfo import CropsGrowthInfo
from alipay.aop.api.domain.AgWeatherMonthlyStats import AgWeatherMonthlyStats
from alipay.aop.api.domain.CropsSoilMoistureInfo import CropsSoilMoistureInfo
from alipay.aop.api.domain.AgWeatherDisasterHistory import AgWeatherDisasterHistory
from alipay.aop.api.domain.AgWeatherDisasterInfo import AgWeatherDisasterInfo
from alipay.aop.api.domain.AgWeatherForecastInfo import AgWeatherForecastInfo
from alipay.aop.api.domain.AgWeatherWeeklyStats import AgWeatherWeeklyStats


class AnttechBlockchainDefinDataserviceCropdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceCropdetailQueryResponse, self).__init__()
        self._growth_infos = None
        self._month_weather_infos = None
        self._soil_moisture_infos = None
        self._weather_disaster_history = None
        self._weather_disaster_infos = None
        self._weather_forecast_infos = None
        self._week_weather_infos = None

    @property
    def growth_infos(self):
        return self._growth_infos

    @growth_infos.setter
    def growth_infos(self, value):
        if isinstance(value, list):
            self._growth_infos = list()
            for i in value:
                if isinstance(i, CropsGrowthInfo):
                    self._growth_infos.append(i)
                else:
                    self._growth_infos.append(CropsGrowthInfo.from_alipay_dict(i))
    @property
    def month_weather_infos(self):
        return self._month_weather_infos

    @month_weather_infos.setter
    def month_weather_infos(self, value):
        if isinstance(value, list):
            self._month_weather_infos = list()
            for i in value:
                if isinstance(i, AgWeatherMonthlyStats):
                    self._month_weather_infos.append(i)
                else:
                    self._month_weather_infos.append(AgWeatherMonthlyStats.from_alipay_dict(i))
    @property
    def soil_moisture_infos(self):
        return self._soil_moisture_infos

    @soil_moisture_infos.setter
    def soil_moisture_infos(self, value):
        if isinstance(value, list):
            self._soil_moisture_infos = list()
            for i in value:
                if isinstance(i, CropsSoilMoistureInfo):
                    self._soil_moisture_infos.append(i)
                else:
                    self._soil_moisture_infos.append(CropsSoilMoistureInfo.from_alipay_dict(i))
    @property
    def weather_disaster_history(self):
        return self._weather_disaster_history

    @weather_disaster_history.setter
    def weather_disaster_history(self, value):
        if isinstance(value, AgWeatherDisasterHistory):
            self._weather_disaster_history = value
        else:
            self._weather_disaster_history = AgWeatherDisasterHistory.from_alipay_dict(value)
    @property
    def weather_disaster_infos(self):
        return self._weather_disaster_infos

    @weather_disaster_infos.setter
    def weather_disaster_infos(self, value):
        if isinstance(value, list):
            self._weather_disaster_infos = list()
            for i in value:
                if isinstance(i, AgWeatherDisasterInfo):
                    self._weather_disaster_infos.append(i)
                else:
                    self._weather_disaster_infos.append(AgWeatherDisasterInfo.from_alipay_dict(i))
    @property
    def weather_forecast_infos(self):
        return self._weather_forecast_infos

    @weather_forecast_infos.setter
    def weather_forecast_infos(self, value):
        if isinstance(value, list):
            self._weather_forecast_infos = list()
            for i in value:
                if isinstance(i, AgWeatherForecastInfo):
                    self._weather_forecast_infos.append(i)
                else:
                    self._weather_forecast_infos.append(AgWeatherForecastInfo.from_alipay_dict(i))
    @property
    def week_weather_infos(self):
        return self._week_weather_infos

    @week_weather_infos.setter
    def week_weather_infos(self, value):
        if isinstance(value, list):
            self._week_weather_infos = list()
            for i in value:
                if isinstance(i, AgWeatherWeeklyStats):
                    self._week_weather_infos.append(i)
                else:
                    self._week_weather_infos.append(AgWeatherWeeklyStats.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceCropdetailQueryResponse, self).parse_response_content(response_content)
        if 'growth_infos' in response:
            self.growth_infos = response['growth_infos']
        if 'month_weather_infos' in response:
            self.month_weather_infos = response['month_weather_infos']
        if 'soil_moisture_infos' in response:
            self.soil_moisture_infos = response['soil_moisture_infos']
        if 'weather_disaster_history' in response:
            self.weather_disaster_history = response['weather_disaster_history']
        if 'weather_disaster_infos' in response:
            self.weather_disaster_infos = response['weather_disaster_infos']
        if 'weather_forecast_infos' in response:
            self.weather_forecast_infos = response['weather_forecast_infos']
        if 'week_weather_infos' in response:
            self.week_weather_infos = response['week_weather_infos']
