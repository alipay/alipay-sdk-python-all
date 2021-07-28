#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialQuestionnareTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialQuestionnareTaskQueryResponse, self).__init__()
        self._channel_type = None
        self._collection_type = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_terminate = None
        self._gray_percent = None
        self._interact_type = None
        self._qstn_id = None
        self._qstn_status = None
        self._rmt_qstn_id = None
        self._rmt_qstn_url = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def collection_type(self):
        return self._collection_type

    @collection_type.setter
    def collection_type(self, value):
        self._collection_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def gmt_terminate(self):
        return self._gmt_terminate

    @gmt_terminate.setter
    def gmt_terminate(self, value):
        self._gmt_terminate = value
    @property
    def gray_percent(self):
        return self._gray_percent

    @gray_percent.setter
    def gray_percent(self, value):
        self._gray_percent = value
    @property
    def interact_type(self):
        return self._interact_type

    @interact_type.setter
    def interact_type(self, value):
        self._interact_type = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value
    @property
    def qstn_status(self):
        return self._qstn_status

    @qstn_status.setter
    def qstn_status(self, value):
        self._qstn_status = value
    @property
    def rmt_qstn_id(self):
        return self._rmt_qstn_id

    @rmt_qstn_id.setter
    def rmt_qstn_id(self, value):
        self._rmt_qstn_id = value
    @property
    def rmt_qstn_url(self):
        return self._rmt_qstn_url

    @rmt_qstn_url.setter
    def rmt_qstn_url(self, value):
        self._rmt_qstn_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialQuestionnareTaskQueryResponse, self).parse_response_content(response_content)
        if 'channel_type' in response:
            self.channel_type = response['channel_type']
        if 'collection_type' in response:
            self.collection_type = response['collection_type']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gmt_terminate' in response:
            self.gmt_terminate = response['gmt_terminate']
        if 'gray_percent' in response:
            self.gray_percent = response['gray_percent']
        if 'interact_type' in response:
            self.interact_type = response['interact_type']
        if 'qstn_id' in response:
            self.qstn_id = response['qstn_id']
        if 'qstn_status' in response:
            self.qstn_status = response['qstn_status']
        if 'rmt_qstn_id' in response:
            self.rmt_qstn_id = response['rmt_qstn_id']
        if 'rmt_qstn_url' in response:
            self.rmt_qstn_url = response['rmt_qstn_url']
