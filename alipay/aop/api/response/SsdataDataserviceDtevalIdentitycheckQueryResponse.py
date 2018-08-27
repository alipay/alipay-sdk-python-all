#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceDtevalIdentitycheckQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceDtevalIdentitycheckQueryResponse, self).__init__()
        self._evidence = None
        self._ext_map = None
        self._id_card_no_match_flag = None
        self._name_match_flag = None
        self._push_ant_data_flag = None

    @property
    def evidence(self):
        return self._evidence

    @evidence.setter
    def evidence(self, value):
        self._evidence = value
    @property
    def ext_map(self):
        return self._ext_map

    @ext_map.setter
    def ext_map(self, value):
        self._ext_map = value
    @property
    def id_card_no_match_flag(self):
        return self._id_card_no_match_flag

    @id_card_no_match_flag.setter
    def id_card_no_match_flag(self, value):
        self._id_card_no_match_flag = value
    @property
    def name_match_flag(self):
        return self._name_match_flag

    @name_match_flag.setter
    def name_match_flag(self, value):
        self._name_match_flag = value
    @property
    def push_ant_data_flag(self):
        return self._push_ant_data_flag

    @push_ant_data_flag.setter
    def push_ant_data_flag(self, value):
        self._push_ant_data_flag = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceDtevalIdentitycheckQueryResponse, self).parse_response_content(response_content)
        if 'evidence' in response:
            self.evidence = response['evidence']
        if 'ext_map' in response:
            self.ext_map = response['ext_map']
        if 'id_card_no_match_flag' in response:
            self.id_card_no_match_flag = response['id_card_no_match_flag']
        if 'name_match_flag' in response:
            self.name_match_flag = response['name_match_flag']
        if 'push_ant_data_flag' in response:
            self.push_ant_data_flag = response['push_ant_data_flag']
