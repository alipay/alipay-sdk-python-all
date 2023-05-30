#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaDigitaltorchofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaDigitaltorchofflineQueryResponse, self).__init__()
        self._age_distribution = None
        self._cloth_digital_human_cnt = None
        self._country_distribution = None
        self._digital_images = None
        self._monthly_activity = None
        self._total_digital_torch_bearer = None
        self._total_participants = None

    @property
    def age_distribution(self):
        return self._age_distribution

    @age_distribution.setter
    def age_distribution(self, value):
        self._age_distribution = value
    @property
    def cloth_digital_human_cnt(self):
        return self._cloth_digital_human_cnt

    @cloth_digital_human_cnt.setter
    def cloth_digital_human_cnt(self, value):
        self._cloth_digital_human_cnt = value
    @property
    def country_distribution(self):
        return self._country_distribution

    @country_distribution.setter
    def country_distribution(self, value):
        self._country_distribution = value
    @property
    def digital_images(self):
        return self._digital_images

    @digital_images.setter
    def digital_images(self, value):
        self._digital_images = value
    @property
    def monthly_activity(self):
        return self._monthly_activity

    @monthly_activity.setter
    def monthly_activity(self, value):
        self._monthly_activity = value
    @property
    def total_digital_torch_bearer(self):
        return self._total_digital_torch_bearer

    @total_digital_torch_bearer.setter
    def total_digital_torch_bearer(self, value):
        self._total_digital_torch_bearer = value
    @property
    def total_participants(self):
        return self._total_participants

    @total_participants.setter
    def total_participants(self, value):
        self._total_participants = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaDigitaltorchofflineQueryResponse, self).parse_response_content(response_content)
        if 'age_distribution' in response:
            self.age_distribution = response['age_distribution']
        if 'cloth_digital_human_cnt' in response:
            self.cloth_digital_human_cnt = response['cloth_digital_human_cnt']
        if 'country_distribution' in response:
            self.country_distribution = response['country_distribution']
        if 'digital_images' in response:
            self.digital_images = response['digital_images']
        if 'monthly_activity' in response:
            self.monthly_activity = response['monthly_activity']
        if 'total_digital_torch_bearer' in response:
            self.total_digital_torch_bearer = response['total_digital_torch_bearer']
        if 'total_participants' in response:
            self.total_participants = response['total_participants']
