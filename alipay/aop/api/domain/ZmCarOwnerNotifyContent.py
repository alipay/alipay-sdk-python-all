#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmCarOwnerDrivingLicenseInfo import ZmCarOwnerDrivingLicenseInfo
from alipay.aop.api.domain.ZmCarOwnerIdentityInfo import ZmCarOwnerIdentityInfo
from alipay.aop.api.domain.ZmCarOwnerVehicleInfo import ZmCarOwnerVehicleInfo


class ZmCarOwnerNotifyContent(object):

    def __init__(self):
        self._driving_license_info = None
        self._identity_info = None
        self._open_status = None
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
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.driving_license_info:
            if hasattr(self.driving_license_info, 'to_alipay_dict'):
                params['driving_license_info'] = self.driving_license_info.to_alipay_dict()
            else:
                params['driving_license_info'] = self.driving_license_info
        if self.identity_info:
            if hasattr(self.identity_info, 'to_alipay_dict'):
                params['identity_info'] = self.identity_info.to_alipay_dict()
            else:
                params['identity_info'] = self.identity_info
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.vehicle_info_list:
            if isinstance(self.vehicle_info_list, list):
                for i in range(0, len(self.vehicle_info_list)):
                    element = self.vehicle_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_info_list[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_info_list, 'to_alipay_dict'):
                params['vehicle_info_list'] = self.vehicle_info_list.to_alipay_dict()
            else:
                params['vehicle_info_list'] = self.vehicle_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCarOwnerNotifyContent()
        if 'driving_license_info' in d:
            o.driving_license_info = d['driving_license_info']
        if 'identity_info' in d:
            o.identity_info = d['identity_info']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'vehicle_info_list' in d:
            o.vehicle_info_list = d['vehicle_info_list']
        return o


