#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfAttachQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfAttachQueryResponse, self).__init__()
        self._attachement_id = None
        self._file_path = None
        self._murl = None
        self._nurl = None
        self._turl = None
        self._url = None

    @property
    def attachement_id(self):
        return self._attachement_id

    @attachement_id.setter
    def attachement_id(self, value):
        self._attachement_id = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def murl(self):
        return self._murl

    @murl.setter
    def murl(self, value):
        self._murl = value
    @property
    def nurl(self):
        return self._nurl

    @nurl.setter
    def nurl(self, value):
        self._nurl = value
    @property
    def turl(self):
        return self._turl

    @turl.setter
    def turl(self, value):
        self._turl = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfAttachQueryResponse, self).parse_response_content(response_content)
        if 'attachement_id' in response:
            self.attachement_id = response['attachement_id']
        if 'file_path' in response:
            self.file_path = response['file_path']
        if 'murl' in response:
            self.murl = response['murl']
        if 'nurl' in response:
            self.nurl = response['nurl']
        if 'turl' in response:
            self.turl = response['turl']
        if 'url' in response:
            self.url = response['url']
