#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskIpprofileQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskIpprofileQueryResponse, self).__init__()
        self._ip_active_score = None
        self._ip_address = None
        self._ip_as_name = None
        self._ip_asn = None
        self._ip_carrier_city = None
        self._ip_carrier_district = None
        self._ip_carrier_province = None
        self._ip_gps_city = None
        self._ip_gps_district = None
        self._ip_gps_province = None
        self._ip_latitude = None
        self._ip_longitude = None
        self._ip_net_id = None
        self._ip_not_human_score = None
        self._ip_opt_desc = None
        self._is_case_threemonth = None
        self._is_cellular_ip = None
        self._is_edu_ip = None
        self._is_idc_ip = None
        self._is_oversea_ip = None
        self._is_proxy_ip = None
        self._net_cert_ratio = None
        self._net_city_ratio = None
        self._net_district_ratio = None
        self._net_phone_ratio = None
        self._net_ratio_norm = None
        self._riskcode = None
        self._unique_id = None
        self._usage_time_type = None
        self._user_cnt_halfyear = None
        self._user_cnt_weekavg = None
        self._user_cnt_weekstddev = None
        self._user_stability = None

    @property
    def ip_active_score(self):
        return self._ip_active_score

    @ip_active_score.setter
    def ip_active_score(self, value):
        self._ip_active_score = value
    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value
    @property
    def ip_as_name(self):
        return self._ip_as_name

    @ip_as_name.setter
    def ip_as_name(self, value):
        self._ip_as_name = value
    @property
    def ip_asn(self):
        return self._ip_asn

    @ip_asn.setter
    def ip_asn(self, value):
        self._ip_asn = value
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
    def ip_net_id(self):
        return self._ip_net_id

    @ip_net_id.setter
    def ip_net_id(self, value):
        self._ip_net_id = value
    @property
    def ip_not_human_score(self):
        return self._ip_not_human_score

    @ip_not_human_score.setter
    def ip_not_human_score(self, value):
        self._ip_not_human_score = value
    @property
    def ip_opt_desc(self):
        return self._ip_opt_desc

    @ip_opt_desc.setter
    def ip_opt_desc(self, value):
        self._ip_opt_desc = value
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
    def net_city_ratio(self):
        return self._net_city_ratio

    @net_city_ratio.setter
    def net_city_ratio(self, value):
        self._net_city_ratio = value
    @property
    def net_district_ratio(self):
        return self._net_district_ratio

    @net_district_ratio.setter
    def net_district_ratio(self, value):
        self._net_district_ratio = value
    @property
    def net_phone_ratio(self):
        return self._net_phone_ratio

    @net_phone_ratio.setter
    def net_phone_ratio(self, value):
        self._net_phone_ratio = value
    @property
    def net_ratio_norm(self):
        return self._net_ratio_norm

    @net_ratio_norm.setter
    def net_ratio_norm(self, value):
        self._net_ratio_norm = value
    @property
    def riskcode(self):
        return self._riskcode

    @riskcode.setter
    def riskcode(self, value):
        if isinstance(value, list):
            self._riskcode = list()
            for i in value:
                self._riskcode.append(i)
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
        response = super(SsdataDataserviceRiskIpprofileQueryResponse, self).parse_response_content(response_content)
        if 'ip_active_score' in response:
            self.ip_active_score = response['ip_active_score']
        if 'ip_address' in response:
            self.ip_address = response['ip_address']
        if 'ip_as_name' in response:
            self.ip_as_name = response['ip_as_name']
        if 'ip_asn' in response:
            self.ip_asn = response['ip_asn']
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
        if 'ip_net_id' in response:
            self.ip_net_id = response['ip_net_id']
        if 'ip_not_human_score' in response:
            self.ip_not_human_score = response['ip_not_human_score']
        if 'ip_opt_desc' in response:
            self.ip_opt_desc = response['ip_opt_desc']
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
        if 'net_city_ratio' in response:
            self.net_city_ratio = response['net_city_ratio']
        if 'net_district_ratio' in response:
            self.net_district_ratio = response['net_district_ratio']
        if 'net_phone_ratio' in response:
            self.net_phone_ratio = response['net_phone_ratio']
        if 'net_ratio_norm' in response:
            self.net_ratio_norm = response['net_ratio_norm']
        if 'riskcode' in response:
            self.riskcode = response['riskcode']
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
