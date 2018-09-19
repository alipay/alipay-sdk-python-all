#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CPCommServices import CPCommServices


class AlipayEcoCplifeCommunityDetailsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeCommunityDetailsQueryResponse, self).__init__()
        self._associated_pois = None
        self._audit_status = None
        self._city_code = None
        self._community_address = None
        self._community_locations = None
        self._community_name = None
        self._community_services = None
        self._community_status = None
        self._district_code = None
        self._gmt_created = None
        self._gmt_modified = None
        self._hotline = None
        self._isv_pid = None
        self._merchant_firm_name = None
        self._merchant_pid = None
        self._next_action = None
        self._out_community_id = None
        self._province_code = None
        self._qr_code_image = None

    @property
    def associated_pois(self):
        return self._associated_pois

    @associated_pois.setter
    def associated_pois(self, value):
        if isinstance(value, list):
            self._associated_pois = list()
            for i in value:
                self._associated_pois.append(i)
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def community_address(self):
        return self._community_address

    @community_address.setter
    def community_address(self, value):
        self._community_address = value
    @property
    def community_locations(self):
        return self._community_locations

    @community_locations.setter
    def community_locations(self, value):
        if isinstance(value, list):
            self._community_locations = list()
            for i in value:
                self._community_locations.append(i)
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def community_services(self):
        return self._community_services

    @community_services.setter
    def community_services(self, value):
        if isinstance(value, list):
            self._community_services = list()
            for i in value:
                if isinstance(i, CPCommServices):
                    self._community_services.append(i)
                else:
                    self._community_services.append(CPCommServices.from_alipay_dict(i))
    @property
    def community_status(self):
        return self._community_status

    @community_status.setter
    def community_status(self, value):
        self._community_status = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def gmt_created(self):
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, value):
        self._gmt_created = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def hotline(self):
        return self._hotline

    @hotline.setter
    def hotline(self, value):
        self._hotline = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_firm_name(self):
        return self._merchant_firm_name

    @merchant_firm_name.setter
    def merchant_firm_name(self, value):
        self._merchant_firm_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, value):
        self._next_action = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def qr_code_image(self):
        return self._qr_code_image

    @qr_code_image.setter
    def qr_code_image(self, value):
        self._qr_code_image = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeCommunityDetailsQueryResponse, self).parse_response_content(response_content)
        if 'associated_pois' in response:
            self.associated_pois = response['associated_pois']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'community_address' in response:
            self.community_address = response['community_address']
        if 'community_locations' in response:
            self.community_locations = response['community_locations']
        if 'community_name' in response:
            self.community_name = response['community_name']
        if 'community_services' in response:
            self.community_services = response['community_services']
        if 'community_status' in response:
            self.community_status = response['community_status']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'gmt_created' in response:
            self.gmt_created = response['gmt_created']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'hotline' in response:
            self.hotline = response['hotline']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'merchant_firm_name' in response:
            self.merchant_firm_name = response['merchant_firm_name']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'next_action' in response:
            self.next_action = response['next_action']
        if 'out_community_id' in response:
            self.out_community_id = response['out_community_id']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'qr_code_image' in response:
            self.qr_code_image = response['qr_code_image']
