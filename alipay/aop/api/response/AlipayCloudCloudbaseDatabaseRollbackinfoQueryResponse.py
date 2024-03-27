#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MongoRollbackInfo import MongoRollbackInfo


class AlipayCloudCloudbaseDatabaseRollbackinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseDatabaseRollbackinfoQueryResponse, self).__init__()
        self._rollback_infos = None

    @property
    def rollback_infos(self):
        return self._rollback_infos

    @rollback_infos.setter
    def rollback_infos(self, value):
        if isinstance(value, list):
            self._rollback_infos = list()
            for i in value:
                if isinstance(i, MongoRollbackInfo):
                    self._rollback_infos.append(i)
                else:
                    self._rollback_infos.append(MongoRollbackInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseDatabaseRollbackinfoQueryResponse, self).parse_response_content(response_content)
        if 'rollback_infos' in response:
            self.rollback_infos = response['rollback_infos']
