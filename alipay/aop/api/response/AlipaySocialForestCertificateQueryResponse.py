#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlantPlace import PlantPlace
from alipay.aop.api.domain.UserCert import UserCert


class AlipaySocialForestCertificateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialForestCertificateQueryResponse, self).__init__()
        self._cert_count_by_tree = None
        self._forest_user = None
        self._plant_place_info = None
        self._total_carbon_amount = None
        self._total_carbon_count = None
        self._total_cert_count = None
        self._user_certs = None

    @property
    def cert_count_by_tree(self):
        return self._cert_count_by_tree

    @cert_count_by_tree.setter
    def cert_count_by_tree(self, value):
        self._cert_count_by_tree = value
    @property
    def forest_user(self):
        return self._forest_user

    @forest_user.setter
    def forest_user(self, value):
        self._forest_user = value
    @property
    def plant_place_info(self):
        return self._plant_place_info

    @plant_place_info.setter
    def plant_place_info(self, value):
        if isinstance(value, PlantPlace):
            self._plant_place_info = value
        else:
            self._plant_place_info = PlantPlace.from_alipay_dict(value)
    @property
    def total_carbon_amount(self):
        return self._total_carbon_amount

    @total_carbon_amount.setter
    def total_carbon_amount(self, value):
        self._total_carbon_amount = value
    @property
    def total_carbon_count(self):
        return self._total_carbon_count

    @total_carbon_count.setter
    def total_carbon_count(self, value):
        self._total_carbon_count = value
    @property
    def total_cert_count(self):
        return self._total_cert_count

    @total_cert_count.setter
    def total_cert_count(self, value):
        self._total_cert_count = value
    @property
    def user_certs(self):
        return self._user_certs

    @user_certs.setter
    def user_certs(self, value):
        if isinstance(value, UserCert):
            self._user_certs = value
        else:
            self._user_certs = UserCert.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialForestCertificateQueryResponse, self).parse_response_content(response_content)
        if 'cert_count_by_tree' in response:
            self.cert_count_by_tree = response['cert_count_by_tree']
        if 'forest_user' in response:
            self.forest_user = response['forest_user']
        if 'plant_place_info' in response:
            self.plant_place_info = response['plant_place_info']
        if 'total_carbon_amount' in response:
            self.total_carbon_amount = response['total_carbon_amount']
        if 'total_carbon_count' in response:
            self.total_carbon_count = response['total_carbon_count']
        if 'total_cert_count' in response:
            self.total_cert_count = response['total_cert_count']
        if 'user_certs' in response:
            self.user_certs = response['user_certs']
