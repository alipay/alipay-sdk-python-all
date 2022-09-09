#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExperimentInfo import ExperimentInfo


class AlipayDigitalopUcdpApeexperimentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApeexperimentQueryResponse, self).__init__()
        self._experiment_info_list = None
        self._running_experiment_id = None

    @property
    def experiment_info_list(self):
        return self._experiment_info_list

    @experiment_info_list.setter
    def experiment_info_list(self, value):
        if isinstance(value, list):
            self._experiment_info_list = list()
            for i in value:
                if isinstance(i, ExperimentInfo):
                    self._experiment_info_list.append(i)
                else:
                    self._experiment_info_list.append(ExperimentInfo.from_alipay_dict(i))
    @property
    def running_experiment_id(self):
        return self._running_experiment_id

    @running_experiment_id.setter
    def running_experiment_id(self, value):
        self._running_experiment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApeexperimentQueryResponse, self).parse_response_content(response_content)
        if 'experiment_info_list' in response:
            self.experiment_info_list = response['experiment_info_list']
        if 'running_experiment_id' in response:
            self.running_experiment_id = response['running_experiment_id']
