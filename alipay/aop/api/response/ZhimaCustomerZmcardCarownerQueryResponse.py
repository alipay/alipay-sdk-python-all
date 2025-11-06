#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZmCarOwnerDrivingLicenseInfo import ZmCarOwnerDrivingLicenseInfo
from alipay.aop.api.domain.ZmCarOwnerIdentityInfo import ZmCarOwnerIdentityInfo
from alipay.aop.api.domain.ZmCarOwnerVehicleInfo import ZmCarOwnerVehicleInfo


class ZhimaCustomerZmcardCarownerQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerZmcardCarownerQueryResponse, self).__init__()
        self._driving_license_info = None
        self._identity_info = None
        self._out_agreement_no = None
        self._vehicle_info_list = None

    @property
    def driving_license_info(self):
        return self._driving_license_info

    @driving_license_info.setter
    def driving_license_info(self, value):
        if isinstance(value, ZmCarOwnerDrivingLicenseInfo):
            self._driving_license_info = value
        else:
            self._driving_license_info = ZmCarOwnerDrivingLicenseInfo.from_alipay_dict(value)
    @property
    def identity_info(self):
        return self._identity_info

    @identity_info.setter
    def identity_info(self, value):
        if isinstance(value, ZmCarOwnerIdentityInfo):
            self._identity_info = value
        else:
            self._identity_info = ZmCarOwnerIdentityInfo.from_alipay_dict(value)
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def vehicle_info_list(self):
        return self._vehicle_info_list

    @vehicle_info_list.setter
    def vehicle_info_list(self, value):
        if isinstance(value, list):
            self._vehicle_info_list = list()
            for i in value:
                if isinstance(i, ZmCarOwnerVehicleInfo):
                    self._vehicle_info_list.append(i)
                else:
                    self._vehicle_info_list.append(ZmCarOwnerVehicleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerZmcardCarownerQueryResponse, self).parse_response_content(response_content)
        if 'driving_license_info' in response:
            self.driving_license_info = response['driving_license_info']
        if 'identity_info' in response:
            self.identity_info = response['identity_info']
        if 'out_agreement_no' in response:
            self.out_agreement_no = response['out_agreement_no']
        if 'vehicle_info_list' in response:
            self.vehicle_info_list = response['vehicle_info_list']
