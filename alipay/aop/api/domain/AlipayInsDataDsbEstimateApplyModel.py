#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayInsDataDsbRequestImageInfo import AlipayInsDataDsbRequestImageInfo


class AlipayInsDataDsbEstimateApplyModel(object):

    def __init__(self):
        self._accident_area_id = None
        self._car_properties = None
        self._case_properties = None
        self._commercial_policy_no = None
        self._compulsory_policy_no = None
        self._engine_no = None
        self._estimate_no = None
        self._estimate_request_uuid = None
        self._frame_no = None
        self._garage_type = None
        self._image_list = None
        self._license_no = None
        self._model_brand = None
        self._new_car_price = None
        self._repair_corp_properties = None
        self._report_no = None
        self._request_timestamp = None
        self._survey_no = None

    @property
    def accident_area_id(self):
        return self._accident_area_id

    @accident_area_id.setter
    def accident_area_id(self, value):
        self._accident_area_id = value
    @property
    def car_properties(self):
        return self._car_properties

    @car_properties.setter
    def car_properties(self, value):
        self._car_properties = value
    @property
    def case_properties(self):
        return self._case_properties

    @case_properties.setter
    def case_properties(self, value):
        self._case_properties = value
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
    def garage_type(self):
        return self._garage_type

    @garage_type.setter
    def garage_type(self, value):
        self._garage_type = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                if isinstance(i, AlipayInsDataDsbRequestImageInfo):
                    self._image_list.append(i)
                else:
                    self._image_list.append(AlipayInsDataDsbRequestImageInfo.from_alipay_dict(i))
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
    def new_car_price(self):
        return self._new_car_price

    @new_car_price.setter
    def new_car_price(self, value):
        self._new_car_price = value
    @property
    def repair_corp_properties(self):
        return self._repair_corp_properties

    @repair_corp_properties.setter
    def repair_corp_properties(self, value):
        self._repair_corp_properties = value
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
        if self.accident_area_id:
            if hasattr(self.accident_area_id, 'to_alipay_dict'):
                params['accident_area_id'] = self.accident_area_id.to_alipay_dict()
            else:
                params['accident_area_id'] = self.accident_area_id
        if self.car_properties:
            if hasattr(self.car_properties, 'to_alipay_dict'):
                params['car_properties'] = self.car_properties.to_alipay_dict()
            else:
                params['car_properties'] = self.car_properties
        if self.case_properties:
            if hasattr(self.case_properties, 'to_alipay_dict'):
                params['case_properties'] = self.case_properties.to_alipay_dict()
            else:
                params['case_properties'] = self.case_properties
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
        if self.garage_type:
            if hasattr(self.garage_type, 'to_alipay_dict'):
                params['garage_type'] = self.garage_type.to_alipay_dict()
            else:
                params['garage_type'] = self.garage_type
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
        if self.new_car_price:
            if hasattr(self.new_car_price, 'to_alipay_dict'):
                params['new_car_price'] = self.new_car_price.to_alipay_dict()
            else:
                params['new_car_price'] = self.new_car_price
        if self.repair_corp_properties:
            if hasattr(self.repair_corp_properties, 'to_alipay_dict'):
                params['repair_corp_properties'] = self.repair_corp_properties.to_alipay_dict()
            else:
                params['repair_corp_properties'] = self.repair_corp_properties
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
        o = AlipayInsDataDsbEstimateApplyModel()
        if 'accident_area_id' in d:
            o.accident_area_id = d['accident_area_id']
        if 'car_properties' in d:
            o.car_properties = d['car_properties']
        if 'case_properties' in d:
            o.case_properties = d['case_properties']
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
        if 'garage_type' in d:
            o.garage_type = d['garage_type']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'model_brand' in d:
            o.model_brand = d['model_brand']
        if 'new_car_price' in d:
            o.new_car_price = d['new_car_price']
        if 'repair_corp_properties' in d:
            o.repair_corp_properties = d['repair_corp_properties']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'request_timestamp' in d:
            o.request_timestamp = d['request_timestamp']
        if 'survey_no' in d:
            o.survey_no = d['survey_no']
        return o


