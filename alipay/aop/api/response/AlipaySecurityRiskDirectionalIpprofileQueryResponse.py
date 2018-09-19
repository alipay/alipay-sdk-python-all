#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskDirectionalIpprofileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskDirectionalIpprofileQueryResponse, self).__init__()
        self._ip_address = None
        self._ip_carrier_city = None
        self._ip_carrier_district = None
        self._ip_carrier_province = None
        self._ip_gps_city = None
        self._ip_gps_district = None
        self._ip_gps_province = None
        self._ip_latitude = None
        self._ip_longitude = None
        self._is_case_threemonth = None
        self._is_cellular_ip = None
        self._is_edu_ip = None
        self._is_idc_ip = None
        self._is_oversea_ip = None
        self._is_proxy_ip = None
        self._net_cert_ratio = None
        self._net_phone_ratio = None
        self._unique_id = None
        self._usage_time_type = None
        self._user_cnt_halfyear = None
        self._user_cnt_weekavg = None
        self._user_cnt_weekstddev = None
        self._user_stability = None

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    @property
    def ip_carrier_city(self):
        return self._ip_carrier_city

    @ip_carrier_city.setter
    def ip_carrier_city(self, value):
        self._ip_carrier_city = value
    @property
    def ip_carrier_district(self):
        return self._ip_carrier_district

    @ip_carrier_district.setter
    def ip_carrier_district(self, value):
        self._ip_carrier_district = value
    @property
    def ip_carrier_province(self):
        return self._ip_carrier_province

    @ip_carrier_province.setter
    def ip_carrier_province(self, value):
        self._ip_carrier_province = value
    @property
    def ip_gps_city(self):
        return self._ip_gps_city

    @ip_gps_city.setter
    def ip_gps_city(self, value):
        self._ip_gps_city = value
    @property
    def ip_gps_district(self):
        return self._ip_gps_district

    @ip_gps_district.setter
    def ip_gps_district(self, value):
        self._ip_gps_district = value
    @property
    def ip_gps_province(self):
        return self._ip_gps_province

    @ip_gps_province.setter
    def ip_gps_province(self, value):
        self._ip_gps_province = value
    @property
    def ip_latitude(self):
        return self._ip_latitude

    @ip_latitude.setter
    def ip_latitude(self, value):
        self._ip_latitude = value
    @property
    def ip_longitude(self):
        return self._ip_longitude

    @ip_longitude.setter
    def ip_longitude(self, value):
        self._ip_longitude = value
    @property
    def is_case_threemonth(self):
        return self._is_case_threemonth

    @is_case_threemonth.setter
    def is_case_threemonth(self, value):
        self._is_case_threemonth = value
    @property
    def is_cellular_ip(self):
        return self._is_cellular_ip

    @is_cellular_ip.setter
    def is_cellular_ip(self, value):
        self._is_cellular_ip = value
    @property
    def is_edu_ip(self):
        return self._is_edu_ip

    @is_edu_ip.setter
    def is_edu_ip(self, value):
        self._is_edu_ip = value
    @property
    def is_idc_ip(self):
        return self._is_idc_ip

    @is_idc_ip.setter
    def is_idc_ip(self, value):
        self._is_idc_ip = value
    @property
    def is_oversea_ip(self):
        return self._is_oversea_ip

    @is_oversea_ip.setter
    def is_oversea_ip(self, value):
        self._is_oversea_ip = value
    @property
    def is_proxy_ip(self):
        return self._is_proxy_ip

    @is_proxy_ip.setter
    def is_proxy_ip(self, value):
        self._is_proxy_ip = value
    @property
    def net_cert_ratio(self):
        return self._net_cert_ratio

    @net_cert_ratio.setter
    def net_cert_ratio(self, value):
        self._net_cert_ratio = value
    @property
    def net_phone_ratio(self):
        return self._net_phone_ratio

    @net_phone_ratio.setter
    def net_phone_ratio(self, value):
        self._net_phone_ratio = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def usage_time_type(self):
        return self._usage_time_type

    @usage_time_type.setter
    def usage_time_type(self, value):
        self._usage_time_type = value
    @property
    def user_cnt_halfyear(self):
        return self._user_cnt_halfyear

    @user_cnt_halfyear.setter
    def user_cnt_halfyear(self, value):
        self._user_cnt_halfyear = value
    @property
    def user_cnt_weekavg(self):
        return self._user_cnt_weekavg

    @user_cnt_weekavg.setter
    def user_cnt_weekavg(self, value):
        self._user_cnt_weekavg = value
    @property
    def user_cnt_weekstddev(self):
        return self._user_cnt_weekstddev

    @user_cnt_weekstddev.setter
    def user_cnt_weekstddev(self, value):
        self._user_cnt_weekstddev = value
    @property
    def user_stability(self):
        return self._user_stability

    @user_stability.setter
    def user_stability(self, value):
        self._user_stability = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskDirectionalIpprofileQueryResponse, self).parse_response_content(response_content)
        if 'ip_address' in response:
            self.ip_address = response['ip_address']
        if 'ip_carrier_city' in response:
            self.ip_carrier_city = response['ip_carrier_city']
        if 'ip_carrier_district' in response:
            self.ip_carrier_district = response['ip_carrier_district']
        if 'ip_carrier_province' in response:
            self.ip_carrier_province = response['ip_carrier_province']
        if 'ip_gps_city' in response:
            self.ip_gps_city = response['ip_gps_city']
        if 'ip_gps_district' in response:
            self.ip_gps_district = response['ip_gps_district']
        if 'ip_gps_province' in response:
            self.ip_gps_province = response['ip_gps_province']
        if 'ip_latitude' in response:
            self.ip_latitude = response['ip_latitude']
        if 'ip_longitude' in response:
            self.ip_longitude = response['ip_longitude']
        if 'is_case_threemonth' in response:
            self.is_case_threemonth = response['is_case_threemonth']
        if 'is_cellular_ip' in response:
            self.is_cellular_ip = response['is_cellular_ip']
        if 'is_edu_ip' in response:
            self.is_edu_ip = response['is_edu_ip']
        if 'is_idc_ip' in response:
            self.is_idc_ip = response['is_idc_ip']
        if 'is_oversea_ip' in response:
            self.is_oversea_ip = response['is_oversea_ip']
        if 'is_proxy_ip' in response:
            self.is_proxy_ip = response['is_proxy_ip']
        if 'net_cert_ratio' in response:
            self.net_cert_ratio = response['net_cert_ratio']
        if 'net_phone_ratio' in response:
            self.net_phone_ratio = response['net_phone_ratio']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
        if 'usage_time_type' in response:
            self.usage_time_type = response['usage_time_type']
        if 'user_cnt_halfyear' in response:
            self.user_cnt_halfyear = response['user_cnt_halfyear']
        if 'user_cnt_weekavg' in response:
            self.user_cnt_weekavg = response['user_cnt_weekavg']
        if 'user_cnt_weekstddev' in response:
            self.user_cnt_weekstddev = response['user_cnt_weekstddev']
        if 'user_stability' in response:
            self.user_stability = response['user_stability']
