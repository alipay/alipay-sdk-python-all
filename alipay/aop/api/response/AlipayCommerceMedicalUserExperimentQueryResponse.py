#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExperimentDetail import ExperimentDetail


class AlipayCommerceMedicalUserExperimentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalUserExperimentQueryResponse, self).__init__()
        self._experiment_detail = None

    @property
    def experiment_detail(self):
        return self._experiment_detail

    @experiment_detail.setter
    def experiment_detail(self, value):
        if isinstance(value, ExperimentDetail):
            self._experiment_detail = value
        else:
            self._experiment_detail = ExperimentDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalUserExperimentQueryResponse, self).parse_response_content(response_content)
        if 'experiment_detail' in response:
            self.experiment_detail = response['experiment_detail']
