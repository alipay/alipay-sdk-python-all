#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractManagerAttachmentsSyncrequest import ContractManagerAttachmentsSyncrequest
from alipay.aop.api.domain.ContractManagerParticipantsSyncRequest import ContractManagerParticipantsSyncRequest
from alipay.aop.api.domain.ContractManagerSignDocsRequest import ContractManagerSignDocsRequest


class ContractManagerProcessSyncRequest(object):

    def __init__(self):
        self._abstract_content = None
        self._attachments = None
        self._business_scene = None
        self._contract_deadline_time = None
        self._flow_end_time = None
        self._flow_id = None
        self._flow_start_time = None
        self._flow_status = None
        self._flow_type = None
        self._merchant_id = None
        self._participants = None
        self._sign_deadline_time = None
        self._sign_docs = None
        self._tags = None

    @property
    def abstract_content(self):
        return self._abstract_content

    @abstract_content.setter
    def abstract_content(self, value):
        self._abstract_content = value
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, ContractManagerAttachmentsSyncrequest):
                    self._attachments.append(i)
                else:
                    self._attachments.append(ContractManagerAttachmentsSyncrequest.from_alipay_dict(i))
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def contract_deadline_time(self):
        return self._contract_deadline_time

    @contract_deadline_time.setter
    def contract_deadline_time(self, value):
        self._contract_deadline_time = value
    @property
    def flow_end_time(self):
        return self._flow_end_time

    @flow_end_time.setter
    def flow_end_time(self, value):
        self._flow_end_time = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def flow_start_time(self):
        return self._flow_start_time

    @flow_start_time.setter
    def flow_start_time(self, value):
        self._flow_start_time = value
    @property
    def flow_status(self):
        return self._flow_status

    @flow_status.setter
    def flow_status(self, value):
        self._flow_status = value
    @property
    def flow_type(self):
        return self._flow_type

    @flow_type.setter
    def flow_type(self, value):
        self._flow_type = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        if isinstance(value, list):
            self._participants = list()
            for i in value:
                if isinstance(i, ContractManagerParticipantsSyncRequest):
                    self._participants.append(i)
                else:
                    self._participants.append(ContractManagerParticipantsSyncRequest.from_alipay_dict(i))
    @property
    def sign_deadline_time(self):
        return self._sign_deadline_time

    @sign_deadline_time.setter
    def sign_deadline_time(self, value):
        self._sign_deadline_time = value
    @property
    def sign_docs(self):
        return self._sign_docs

    @sign_docs.setter
    def sign_docs(self, value):
        if isinstance(value, list):
            self._sign_docs = list()
            for i in value:
                if isinstance(i, ContractManagerSignDocsRequest):
                    self._sign_docs.append(i)
                else:
                    self._sign_docs.append(ContractManagerSignDocsRequest.from_alipay_dict(i))
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.abstract_content:
            if hasattr(self.abstract_content, 'to_alipay_dict'):
                params['abstract_content'] = self.abstract_content.to_alipay_dict()
            else:
                params['abstract_content'] = self.abstract_content
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.contract_deadline_time:
            if hasattr(self.contract_deadline_time, 'to_alipay_dict'):
                params['contract_deadline_time'] = self.contract_deadline_time.to_alipay_dict()
            else:
                params['contract_deadline_time'] = self.contract_deadline_time
        if self.flow_end_time:
            if hasattr(self.flow_end_time, 'to_alipay_dict'):
                params['flow_end_time'] = self.flow_end_time.to_alipay_dict()
            else:
                params['flow_end_time'] = self.flow_end_time
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.flow_start_time:
            if hasattr(self.flow_start_time, 'to_alipay_dict'):
                params['flow_start_time'] = self.flow_start_time.to_alipay_dict()
            else:
                params['flow_start_time'] = self.flow_start_time
        if self.flow_status:
            if hasattr(self.flow_status, 'to_alipay_dict'):
                params['flow_status'] = self.flow_status.to_alipay_dict()
            else:
                params['flow_status'] = self.flow_status
        if self.flow_type:
            if hasattr(self.flow_type, 'to_alipay_dict'):
                params['flow_type'] = self.flow_type.to_alipay_dict()
            else:
                params['flow_type'] = self.flow_type
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.participants:
            if isinstance(self.participants, list):
                for i in range(0, len(self.participants)):
                    element = self.participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participants[i] = element.to_alipay_dict()
            if hasattr(self.participants, 'to_alipay_dict'):
                params['participants'] = self.participants.to_alipay_dict()
            else:
                params['participants'] = self.participants
        if self.sign_deadline_time:
            if hasattr(self.sign_deadline_time, 'to_alipay_dict'):
                params['sign_deadline_time'] = self.sign_deadline_time.to_alipay_dict()
            else:
                params['sign_deadline_time'] = self.sign_deadline_time
        if self.sign_docs:
            if isinstance(self.sign_docs, list):
                for i in range(0, len(self.sign_docs)):
                    element = self.sign_docs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_docs[i] = element.to_alipay_dict()
            if hasattr(self.sign_docs, 'to_alipay_dict'):
                params['sign_docs'] = self.sign_docs.to_alipay_dict()
            else:
                params['sign_docs'] = self.sign_docs
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractManagerProcessSyncRequest()
        if 'abstract_content' in d:
            o.abstract_content = d['abstract_content']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'contract_deadline_time' in d:
            o.contract_deadline_time = d['contract_deadline_time']
        if 'flow_end_time' in d:
            o.flow_end_time = d['flow_end_time']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'flow_start_time' in d:
            o.flow_start_time = d['flow_start_time']
        if 'flow_status' in d:
            o.flow_status = d['flow_status']
        if 'flow_type' in d:
            o.flow_type = d['flow_type']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'participants' in d:
            o.participants = d['participants']
        if 'sign_deadline_time' in d:
            o.sign_deadline_time = d['sign_deadline_time']
        if 'sign_docs' in d:
            o.sign_docs = d['sign_docs']
        if 'tags' in d:
            o.tags = d['tags']
        return o


