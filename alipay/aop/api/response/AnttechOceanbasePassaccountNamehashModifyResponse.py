#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassAccountNameHashRecordDTO import PassAccountNameHashRecordDTO


class AnttechOceanbasePassaccountNamehashModifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassaccountNamehashModifyResponse, self).__init__()
        self._affected_rows = None
        self._can_execute = None
        self._conflict_count = None
        self._data_source = None
        self._items = None
        self._precheck = None
        self._ready_count = None
        self._selected_count = None
        self._snapshot_token = None

    @property
    def affected_rows(self):
        return self._affected_rows

    @affected_rows.setter
    def affected_rows(self, value):
        self._affected_rows = value
    @property
    def can_execute(self):
        return self._can_execute

    @can_execute.setter
    def can_execute(self, value):
        self._can_execute = value
    @property
    def conflict_count(self):
        return self._conflict_count

    @conflict_count.setter
    def conflict_count(self, value):
        self._conflict_count = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, PassAccountNameHashRecordDTO):
                    self._items.append(i)
                else:
                    self._items.append(PassAccountNameHashRecordDTO.from_alipay_dict(i))
    @property
    def precheck(self):
        return self._precheck

    @precheck.setter
    def precheck(self, value):
        self._precheck = value
    @property
    def ready_count(self):
        return self._ready_count

    @ready_count.setter
    def ready_count(self, value):
        self._ready_count = value
    @property
    def selected_count(self):
        return self._selected_count

    @selected_count.setter
    def selected_count(self, value):
        self._selected_count = value
    @property
    def snapshot_token(self):
        return self._snapshot_token

    @snapshot_token.setter
    def snapshot_token(self, value):
        self._snapshot_token = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassaccountNamehashModifyResponse, self).parse_response_content(response_content)
        if 'affected_rows' in response:
            self.affected_rows = response['affected_rows']
        if 'can_execute' in response:
            self.can_execute = response['can_execute']
        if 'conflict_count' in response:
            self.conflict_count = response['conflict_count']
        if 'data_source' in response:
            self.data_source = response['data_source']
        if 'items' in response:
            self.items = response['items']
        if 'precheck' in response:
            self.precheck = response['precheck']
        if 'ready_count' in response:
            self.ready_count = response['ready_count']
        if 'selected_count' in response:
            self.selected_count = response['selected_count']
        if 'snapshot_token' in response:
            self.snapshot_token = response['snapshot_token']
