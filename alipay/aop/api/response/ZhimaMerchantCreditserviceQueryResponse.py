#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseInfoApiConfig import BaseInfoApiConfig
from alipay.aop.api.domain.RiskApiConfig import RiskApiConfig
from alipay.aop.api.domain.PromiseApiConfig import PromiseApiConfig
from alipay.aop.api.domain.RiskApiConfig import RiskApiConfig


class ZhimaMerchantCreditserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantCreditserviceQueryResponse, self).__init__()
        self._base_info_config = None
        self._create_type = None
        self._credit_service_id = None
        self._evaluation_risk_configs = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_offline = None
        self._gmt_online = None
        self._gmt_review = None
        self._isv_id = None
        self._merchant_id = None
        self._merchant_name = None
        self._mini_app_id = None
        self._process_id = None
        self._promise_config = None
        self._review_failed_msg = None
        self._review_status = None
        self._risk_config = None
        self._status = None
        self._version_no = None

    @property
    def base_info_config(self):
        return self._base_info_config

    @base_info_config.setter
    def base_info_config(self, value):
        if isinstance(value, BaseInfoApiConfig):
            self._base_info_config = value
        else:
            self._base_info_config = BaseInfoApiConfig.from_alipay_dict(value)
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def credit_service_id(self):
        return self._credit_service_id

    @credit_service_id.setter
    def credit_service_id(self, value):
        self._credit_service_id = value
    @property
    def evaluation_risk_configs(self):
        return self._evaluation_risk_configs

    @evaluation_risk_configs.setter
    def evaluation_risk_configs(self, value):
        if isinstance(value, list):
            self._evaluation_risk_configs = list()
            for i in value:
                if isinstance(i, RiskApiConfig):
                    self._evaluation_risk_configs.append(i)
                else:
                    self._evaluation_risk_configs.append(RiskApiConfig.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_offline(self):
        return self._gmt_offline

    @gmt_offline.setter
    def gmt_offline(self, value):
        self._gmt_offline = value
    @property
    def gmt_online(self):
        return self._gmt_online

    @gmt_online.setter
    def gmt_online(self, value):
        self._gmt_online = value
    @property
    def gmt_review(self):
        return self._gmt_review

    @gmt_review.setter
    def gmt_review(self, value):
        self._gmt_review = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseApiConfig):
            self._promise_config = value
        else:
            self._promise_config = PromiseApiConfig.from_alipay_dict(value)
    @property
    def review_failed_msg(self):
        return self._review_failed_msg

    @review_failed_msg.setter
    def review_failed_msg(self, value):
        self._review_failed_msg = value
    @property
    def review_status(self):
        return self._review_status

    @review_status.setter
    def review_status(self, value):
        self._review_status = value
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskApiConfig):
            self._risk_config = value
        else:
            self._risk_config = RiskApiConfig.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantCreditserviceQueryResponse, self).parse_response_content(response_content)
        if 'base_info_config' in response:
            self.base_info_config = response['base_info_config']
        if 'create_type' in response:
            self.create_type = response['create_type']
        if 'credit_service_id' in response:
            self.credit_service_id = response['credit_service_id']
        if 'evaluation_risk_configs' in response:
            self.evaluation_risk_configs = response['evaluation_risk_configs']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gmt_offline' in response:
            self.gmt_offline = response['gmt_offline']
        if 'gmt_online' in response:
            self.gmt_online = response['gmt_online']
        if 'gmt_review' in response:
            self.gmt_review = response['gmt_review']
        if 'isv_id' in response:
            self.isv_id = response['isv_id']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'promise_config' in response:
            self.promise_config = response['promise_config']
        if 'review_failed_msg' in response:
            self.review_failed_msg = response['review_failed_msg']
        if 'review_status' in response:
            self.review_status = response['review_status']
        if 'risk_config' in response:
            self.risk_config = response['risk_config']
        if 'status' in response:
            self.status = response['status']
        if 'version_no' in response:
            self.version_no = response['version_no']
