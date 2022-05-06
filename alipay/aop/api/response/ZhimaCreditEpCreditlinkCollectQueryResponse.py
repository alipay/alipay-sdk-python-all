#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DataFile import DataFile


class ZhimaCreditEpCreditlinkCollectQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkCollectQueryResponse, self).__init__()
        self._data_status = None
        self._data_type = None
        self._encrypt_model = None
        self._file_list = None
        self._file_num = None
        self._files = None
        self._merchant_request_id = None
        self._secret = None

    @property
    def data_status(self):
        return self._data_status

    @data_status.setter
    def data_status(self, value):
        self._data_status = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def encrypt_model(self):
        return self._encrypt_model

    @encrypt_model.setter
    def encrypt_model(self, value):
        self._encrypt_model = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                self._file_list.append(i)
    @property
    def file_num(self):
        return self._file_num

    @file_num.setter
    def file_num(self, value):
        self._file_num = value
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = list()
            for i in value:
                if isinstance(i, DataFile):
                    self._files.append(i)
                else:
                    self._files.append(DataFile.from_alipay_dict(i))
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkCollectQueryResponse, self).parse_response_content(response_content)
        if 'data_status' in response:
            self.data_status = response['data_status']
        if 'data_type' in response:
            self.data_type = response['data_type']
        if 'encrypt_model' in response:
            self.encrypt_model = response['encrypt_model']
        if 'file_list' in response:
            self.file_list = response['file_list']
        if 'file_num' in response:
            self.file_num = response['file_num']
        if 'files' in response:
            self.files = response['files']
        if 'merchant_request_id' in response:
            self.merchant_request_id = response['merchant_request_id']
        if 'secret' in response:
            self.secret = response['secret']
