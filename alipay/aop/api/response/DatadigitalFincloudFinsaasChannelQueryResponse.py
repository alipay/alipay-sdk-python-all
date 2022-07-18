#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelRuleDTO import ChannelRuleDTO


class DatadigitalFincloudFinsaasChannelQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasChannelQueryResponse, self).__init__()
        self._channel_code = None
        self._channel_desc = None
        self._channel_name = None
        self._channel_rule = None
        self._channel_scope = None
        self._channel_status = None
        self._channel_template = None
        self._channel_tenant_code = None
        self._channel_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._pic_url = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_desc(self):
        return self._channel_desc

    @channel_desc.setter
    def channel_desc(self, value):
        self._channel_desc = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def channel_rule(self):
        return self._channel_rule

    @channel_rule.setter
    def channel_rule(self, value):
        if isinstance(value, ChannelRuleDTO):
            self._channel_rule = value
        else:
            self._channel_rule = ChannelRuleDTO.from_alipay_dict(value)
    @property
    def channel_scope(self):
        return self._channel_scope

    @channel_scope.setter
    def channel_scope(self, value):
        self._channel_scope = value
    @property
    def channel_status(self):
        return self._channel_status

    @channel_status.setter
    def channel_status(self, value):
        self._channel_status = value
    @property
    def channel_template(self):
        return self._channel_template

    @channel_template.setter
    def channel_template(self, value):
        self._channel_template = value
    @property
    def channel_tenant_code(self):
        return self._channel_tenant_code

    @channel_tenant_code.setter
    def channel_tenant_code(self, value):
        self._channel_tenant_code = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasChannelQueryResponse, self).parse_response_content(response_content)
        if 'channel_code' in response:
            self.channel_code = response['channel_code']
        if 'channel_desc' in response:
            self.channel_desc = response['channel_desc']
        if 'channel_name' in response:
            self.channel_name = response['channel_name']
        if 'channel_rule' in response:
            self.channel_rule = response['channel_rule']
        if 'channel_scope' in response:
            self.channel_scope = response['channel_scope']
        if 'channel_status' in response:
            self.channel_status = response['channel_status']
        if 'channel_template' in response:
            self.channel_template = response['channel_template']
        if 'channel_tenant_code' in response:
            self.channel_tenant_code = response['channel_tenant_code']
        if 'channel_type' in response:
            self.channel_type = response['channel_type']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'id' in response:
            self.id = response['id']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
