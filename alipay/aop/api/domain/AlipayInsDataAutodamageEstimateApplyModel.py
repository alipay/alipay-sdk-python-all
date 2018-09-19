#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayInsDataAutodamageRequestImageInfo import AlipayInsDataAutodamageRequestImageInfo


class AlipayInsDataAutodamageEstimateApplyModel(object):

    def __init__(self):
        self._commercial_policy_no = None
        self._compulsory_policy_no = None
        self._engine_no = None
        self._estimate_no = None
        self._estimate_request_uuid = None
        self._frame_no = None
        self._image_list = None
        self._license_no = None
        self._model_brand = None
        self._report_no = None
        self._request_timestamp = None
        self._survey_no = None

    @property
    def commercial_policy_no(self):
        return self._commercial_policy_no

    @commercial_policy_no.setter
    def commercial_policy_no(self, value):
        self._commercial_policy_no = value
    @property
    def compulsory_policy_no(self):
        return self._compulsory_policy_no

    @compulsory_policy_no.setter
    def compulsory_policy_no(self, value):
        self._compulsory_policy_no = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def estimate_request_uuid(self):
        return self._estimate_request_uuid

    @estimate_request_uuid.setter
    def estimate_request_uuid(self, value):
        self._estimate_request_uuid = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                if isinstance(i, AlipayInsDataAutodamageRequestImageInfo):
                    self._image_list.append(i)
                else:
                    self._image_list.append(AlipayInsDataAutodamageRequestImageInfo.from_alipay_dict(i))
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def model_brand(self):
        return self._model_brand

    @model_brand.setter
    def model_brand(self, value):
        self._model_brand = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def request_timestamp(self):
        return self._request_timestamp

    @request_timestamp.setter
    def request_timestamp(self, value):
        self._request_timestamp = value
    @property
    def survey_no(self):
        return self._survey_no

    @survey_no.setter
    def survey_no(self, value):
        self._survey_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.commercial_policy_no:
            if hasattr(self.commercial_policy_no, 'to_alipay_dict'):
                params['commercial_policy_no'] = self.commercial_policy_no.to_alipay_dict()
            else:
                params['commercial_policy_no'] = self.commercial_policy_no
        if self.compulsory_policy_no:
            if hasattr(self.compulsory_policy_no, 'to_alipay_dict'):
                params['compulsory_policy_no'] = self.compulsory_policy_no.to_alipay_dict()
            else:
                params['compulsory_policy_no'] = self.compulsory_policy_no
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.estimate_no:
            if hasattr(self.estimate_no, 'to_alipay_dict'):
                params['estimate_no'] = self.estimate_no.to_alipay_dict()
            else:
                params['estimate_no'] = self.estimate_no
        if self.estimate_request_uuid:
            if hasattr(self.estimate_request_uuid, 'to_alipay_dict'):
                params['estimate_request_uuid'] = self.estimate_request_uuid.to_alipay_dict()
            else:
                params['estimate_request_uuid'] = self.estimate_request_uuid
        if self.frame_no:
            if hasattr(self.frame_no, 'to_alipay_dict'):
                params['frame_no'] = self.frame_no.to_alipay_dict()
            else:
                params['frame_no'] = self.frame_no
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.model_brand:
            if hasattr(self.model_brand, 'to_alipay_dict'):
                params['model_brand'] = self.model_brand.to_alipay_dict()
            else:
                params['model_brand'] = self.model_brand
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.request_timestamp:
            if hasattr(self.request_timestamp, 'to_alipay_dict'):
                params['request_timestamp'] = self.request_timestamp.to_alipay_dict()
            else:
                params['request_timestamp'] = self.request_timestamp
        if self.survey_no:
            if hasattr(self.survey_no, 'to_alipay_dict'):
                params['survey_no'] = self.survey_no.to_alipay_dict()
            else:
                params['survey_no'] = self.survey_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutodamageEstimateApplyModel()
        if 'commercial_policy_no' in d:
            o.commercial_policy_no = d['commercial_policy_no']
        if 'compulsory_policy_no' in d:
            o.compulsory_policy_no = d['compulsory_policy_no']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'estimate_no' in d:
            o.estimate_no = d['estimate_no']
        if 'estimate_request_uuid' in d:
            o.estimate_request_uuid = d['estimate_request_uuid']
        if 'frame_no' in d:
            o.frame_no = d['frame_no']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'model_brand' in d:
            o.model_brand = d['model_brand']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'request_timestamp' in d:
            o.request_timestamp = d['request_timestamp']
        if 'survey_no' in d:
            o.survey_no = d['survey_no']
        return o


