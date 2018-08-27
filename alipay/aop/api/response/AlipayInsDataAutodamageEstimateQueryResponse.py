#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsDataAutodamageEstimateResultDetailModel import InsDataAutodamageEstimateResultDetailModel


class AlipayInsDataAutodamageEstimateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataAutodamageEstimateQueryResponse, self).__init__()
        self._commercial_policy_no = None
        self._compulsory_policy_no = None
        self._engine_no = None
        self._estimate_detail_list = None
        self._estimate_no = None
        self._frame_no = None
        self._license_no = None
        self._model_brand = None
        self._report_no = None
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
    def estimate_detail_list(self):
        return self._estimate_detail_list

    @estimate_detail_list.setter
    def estimate_detail_list(self, value):
        if isinstance(value, list):
            self._estimate_detail_list = list()
            for i in value:
                if isinstance(i, InsDataAutodamageEstimateResultDetailModel):
                    self._estimate_detail_list.append(i)
                else:
                    self._estimate_detail_list.append(InsDataAutodamageEstimateResultDetailModel.from_alipay_dict(i))
    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
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
    def survey_no(self):
        return self._survey_no

    @survey_no.setter
    def survey_no(self, value):
        self._survey_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataAutodamageEstimateQueryResponse, self).parse_response_content(response_content)
        if 'commercial_policy_no' in response:
            self.commercial_policy_no = response['commercial_policy_no']
        if 'compulsory_policy_no' in response:
            self.compulsory_policy_no = response['compulsory_policy_no']
        if 'engine_no' in response:
            self.engine_no = response['engine_no']
        if 'estimate_detail_list' in response:
            self.estimate_detail_list = response['estimate_detail_list']
        if 'estimate_no' in response:
            self.estimate_no = response['estimate_no']
        if 'frame_no' in response:
            self.frame_no = response['frame_no']
        if 'license_no' in response:
            self.license_no = response['license_no']
        if 'model_brand' in response:
            self.model_brand = response['model_brand']
        if 'report_no' in response:
            self.report_no = response['report_no']
        if 'survey_no' in response:
            self.survey_no = response['survey_no']
