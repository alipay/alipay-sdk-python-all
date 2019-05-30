#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsHealthGainFlowResult import InsHealthGainFlowResult
from alipay.aop.api.domain.InsHealthGiftBatchAlreadyOpenedResult import InsHealthGiftBatchAlreadyOpenedResult
from alipay.aop.api.domain.InsHealthGiftBatchGainSumInsuredResult import InsHealthGiftBatchGainSumInsuredResult
from alipay.aop.api.domain.InsHealthGiftBatchMySumInsuredResult import InsHealthGiftBatchMySumInsuredResult
from alipay.aop.api.domain.InsHealthGiftBatchValidGiftResult import InsHealthGiftBatchValidGiftResult
from alipay.aop.api.domain.InsHealthSendFlowResult import InsHealthSendFlowResult


class AlipayInsSceneHealthGiftBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthGiftBatchqueryResponse, self).__init__()
        self._gained_sum_insured_by_source = None
        self._health_gain_flow_list = None
        self._health_gift_batch_already_opened_list = None
        self._health_gift_batch_gain_sum_insured_list = None
        self._health_gift_batch_my_sum_insured_list = None
        self._health_gift_batch_valid_gift_list = None
        self._health_send_flow_list = None

    @property
    def gained_sum_insured_by_source(self):
        return self._gained_sum_insured_by_source

    @gained_sum_insured_by_source.setter
    def gained_sum_insured_by_source(self, value):
        self._gained_sum_insured_by_source = value
    @property
    def health_gain_flow_list(self):
        return self._health_gain_flow_list

    @health_gain_flow_list.setter
    def health_gain_flow_list(self, value):
        if isinstance(value, list):
            self._health_gain_flow_list = list()
            for i in value:
                if isinstance(i, InsHealthGainFlowResult):
                    self._health_gain_flow_list.append(i)
                else:
                    self._health_gain_flow_list.append(InsHealthGainFlowResult.from_alipay_dict(i))
    @property
    def health_gift_batch_already_opened_list(self):
        return self._health_gift_batch_already_opened_list

    @health_gift_batch_already_opened_list.setter
    def health_gift_batch_already_opened_list(self, value):
        if isinstance(value, list):
            self._health_gift_batch_already_opened_list = list()
            for i in value:
                if isinstance(i, InsHealthGiftBatchAlreadyOpenedResult):
                    self._health_gift_batch_already_opened_list.append(i)
                else:
                    self._health_gift_batch_already_opened_list.append(InsHealthGiftBatchAlreadyOpenedResult.from_alipay_dict(i))
    @property
    def health_gift_batch_gain_sum_insured_list(self):
        return self._health_gift_batch_gain_sum_insured_list

    @health_gift_batch_gain_sum_insured_list.setter
    def health_gift_batch_gain_sum_insured_list(self, value):
        if isinstance(value, list):
            self._health_gift_batch_gain_sum_insured_list = list()
            for i in value:
                if isinstance(i, InsHealthGiftBatchGainSumInsuredResult):
                    self._health_gift_batch_gain_sum_insured_list.append(i)
                else:
                    self._health_gift_batch_gain_sum_insured_list.append(InsHealthGiftBatchGainSumInsuredResult.from_alipay_dict(i))
    @property
    def health_gift_batch_my_sum_insured_list(self):
        return self._health_gift_batch_my_sum_insured_list

    @health_gift_batch_my_sum_insured_list.setter
    def health_gift_batch_my_sum_insured_list(self, value):
        if isinstance(value, list):
            self._health_gift_batch_my_sum_insured_list = list()
            for i in value:
                if isinstance(i, InsHealthGiftBatchMySumInsuredResult):
                    self._health_gift_batch_my_sum_insured_list.append(i)
                else:
                    self._health_gift_batch_my_sum_insured_list.append(InsHealthGiftBatchMySumInsuredResult.from_alipay_dict(i))
    @property
    def health_gift_batch_valid_gift_list(self):
        return self._health_gift_batch_valid_gift_list

    @health_gift_batch_valid_gift_list.setter
    def health_gift_batch_valid_gift_list(self, value):
        if isinstance(value, list):
            self._health_gift_batch_valid_gift_list = list()
            for i in value:
                if isinstance(i, InsHealthGiftBatchValidGiftResult):
                    self._health_gift_batch_valid_gift_list.append(i)
                else:
                    self._health_gift_batch_valid_gift_list.append(InsHealthGiftBatchValidGiftResult.from_alipay_dict(i))
    @property
    def health_send_flow_list(self):
        return self._health_send_flow_list

    @health_send_flow_list.setter
    def health_send_flow_list(self, value):
        if isinstance(value, list):
            self._health_send_flow_list = list()
            for i in value:
                if isinstance(i, InsHealthSendFlowResult):
                    self._health_send_flow_list.append(i)
                else:
                    self._health_send_flow_list.append(InsHealthSendFlowResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthGiftBatchqueryResponse, self).parse_response_content(response_content)
        if 'gained_sum_insured_by_source' in response:
            self.gained_sum_insured_by_source = response['gained_sum_insured_by_source']
        if 'health_gain_flow_list' in response:
            self.health_gain_flow_list = response['health_gain_flow_list']
        if 'health_gift_batch_already_opened_list' in response:
            self.health_gift_batch_already_opened_list = response['health_gift_batch_already_opened_list']
        if 'health_gift_batch_gain_sum_insured_list' in response:
            self.health_gift_batch_gain_sum_insured_list = response['health_gift_batch_gain_sum_insured_list']
        if 'health_gift_batch_my_sum_insured_list' in response:
            self.health_gift_batch_my_sum_insured_list = response['health_gift_batch_my_sum_insured_list']
        if 'health_gift_batch_valid_gift_list' in response:
            self.health_gift_batch_valid_gift_list = response['health_gift_batch_valid_gift_list']
        if 'health_send_flow_list' in response:
            self.health_send_flow_list = response['health_send_flow_list']
