#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmepBiddingTargetInfo import ZmepBiddingTargetInfo
from alipay.aop.api.domain.ZmepBiddingTargetInfo import ZmepBiddingTargetInfo


class ZmepBiddingInfo(object):

    def __init__(self):
        self._agency_organization = None
        self._bid_winner = None
        self._body = None
        self._candidate = None
        self._gglx = None
        self._publish_time = None
        self._purchasing_agent = None
        self._region = None
        self._role = None
        self._title = None
        self._xmbh = None

    @property
    def agency_organization(self):
        return self._agency_organization

    @agency_organization.setter
    def agency_organization(self, value):
        self._agency_organization = value
    @property
    def bid_winner(self):
        return self._bid_winner

    @bid_winner.setter
    def bid_winner(self, value):
        if isinstance(value, list):
            self._bid_winner = list()
            for i in value:
                if isinstance(i, ZmepBiddingTargetInfo):
                    self._bid_winner.append(i)
                else:
                    self._bid_winner.append(ZmepBiddingTargetInfo.from_alipay_dict(i))
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def candidate(self):
        return self._candidate

    @candidate.setter
    def candidate(self, value):
        if isinstance(value, list):
            self._candidate = list()
            for i in value:
                if isinstance(i, ZmepBiddingTargetInfo):
                    self._candidate.append(i)
                else:
                    self._candidate.append(ZmepBiddingTargetInfo.from_alipay_dict(i))
    @property
    def gglx(self):
        return self._gglx

    @gglx.setter
    def gglx(self, value):
        self._gglx = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def purchasing_agent(self):
        return self._purchasing_agent

    @purchasing_agent.setter
    def purchasing_agent(self, value):
        if isinstance(value, list):
            self._purchasing_agent = list()
            for i in value:
                self._purchasing_agent.append(i)
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if isinstance(value, list):
            self._role = list()
            for i in value:
                self._role.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def xmbh(self):
        return self._xmbh

    @xmbh.setter
    def xmbh(self, value):
        self._xmbh = value


    def to_alipay_dict(self):
        params = dict()
        if self.agency_organization:
            if hasattr(self.agency_organization, 'to_alipay_dict'):
                params['agency_organization'] = self.agency_organization.to_alipay_dict()
            else:
                params['agency_organization'] = self.agency_organization
        if self.bid_winner:
            if isinstance(self.bid_winner, list):
                for i in range(0, len(self.bid_winner)):
                    element = self.bid_winner[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bid_winner[i] = element.to_alipay_dict()
            if hasattr(self.bid_winner, 'to_alipay_dict'):
                params['bid_winner'] = self.bid_winner.to_alipay_dict()
            else:
                params['bid_winner'] = self.bid_winner
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.candidate:
            if isinstance(self.candidate, list):
                for i in range(0, len(self.candidate)):
                    element = self.candidate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.candidate[i] = element.to_alipay_dict()
            if hasattr(self.candidate, 'to_alipay_dict'):
                params['candidate'] = self.candidate.to_alipay_dict()
            else:
                params['candidate'] = self.candidate
        if self.gglx:
            if hasattr(self.gglx, 'to_alipay_dict'):
                params['gglx'] = self.gglx.to_alipay_dict()
            else:
                params['gglx'] = self.gglx
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.purchasing_agent:
            if isinstance(self.purchasing_agent, list):
                for i in range(0, len(self.purchasing_agent)):
                    element = self.purchasing_agent[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.purchasing_agent[i] = element.to_alipay_dict()
            if hasattr(self.purchasing_agent, 'to_alipay_dict'):
                params['purchasing_agent'] = self.purchasing_agent.to_alipay_dict()
            else:
                params['purchasing_agent'] = self.purchasing_agent
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.role:
            if isinstance(self.role, list):
                for i in range(0, len(self.role)):
                    element = self.role[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role[i] = element.to_alipay_dict()
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.xmbh:
            if hasattr(self.xmbh, 'to_alipay_dict'):
                params['xmbh'] = self.xmbh.to_alipay_dict()
            else:
                params['xmbh'] = self.xmbh
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepBiddingInfo()
        if 'agency_organization' in d:
            o.agency_organization = d['agency_organization']
        if 'bid_winner' in d:
            o.bid_winner = d['bid_winner']
        if 'body' in d:
            o.body = d['body']
        if 'candidate' in d:
            o.candidate = d['candidate']
        if 'gglx' in d:
            o.gglx = d['gglx']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'purchasing_agent' in d:
            o.purchasing_agent = d['purchasing_agent']
        if 'region' in d:
            o.region = d['region']
        if 'role' in d:
            o.role = d['role']
        if 'title' in d:
            o.title = d['title']
        if 'xmbh' in d:
            o.xmbh = d['xmbh']
        return o


