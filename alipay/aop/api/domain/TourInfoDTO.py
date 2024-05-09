#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TourPackageInfoDTO import TourPackageInfoDTO


class TourInfoDTO(object):

    def __init__(self):
        self._from_location = None
        self._package_info = None
        self._to_location = None

    @property
    def from_location(self):
        return self._from_location

    @from_location.setter
    def from_location(self, value):
        self._from_location = value
    @property
    def package_info(self):
        return self._package_info

    @package_info.setter
    def package_info(self, value):
        if isinstance(value, TourPackageInfoDTO):
            self._package_info = value
        else:
            self._package_info = TourPackageInfoDTO.from_alipay_dict(value)
    @property
    def to_location(self):
        return self._to_location

    @to_location.setter
    def to_location(self, value):
        self._to_location = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_location:
            if hasattr(self.from_location, 'to_alipay_dict'):
                params['from_location'] = self.from_location.to_alipay_dict()
            else:
                params['from_location'] = self.from_location
        if self.package_info:
            if hasattr(self.package_info, 'to_alipay_dict'):
                params['package_info'] = self.package_info.to_alipay_dict()
            else:
                params['package_info'] = self.package_info
        if self.to_location:
            if hasattr(self.to_location, 'to_alipay_dict'):
                params['to_location'] = self.to_location.to_alipay_dict()
            else:
                params['to_location'] = self.to_location
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourInfoDTO()
        if 'from_location' in d:
            o.from_location = d['from_location']
        if 'package_info' in d:
            o.package_info = d['package_info']
        if 'to_location' in d:
            o.to_location = d['to_location']
        return o


