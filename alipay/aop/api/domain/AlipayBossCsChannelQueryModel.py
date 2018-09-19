#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossCsChannelQueryModel(object):

    def __init__(self):
        self._att = None
        self._connectionrate = None
        self._curragentsloggedin = None
        self._curragenttalking = None
        self._currentnotreadyagents = None
        self._currentreadyagents = None
        self._currnumberwaitingcalls = None
        self._endkey = None
        self._startkey = None
        self._visitorinflow = None
        self._visitorresponse = None
        self._visitorresponsetransfer = None

    @property
    def att(self):
        return self._att

    @att.setter
    def att(self, value):
        self._att = value
    @property
    def connectionrate(self):
        return self._connectionrate

    @connectionrate.setter
    def connectionrate(self, value):
        self._connectionrate = value
    @property
    def curragentsloggedin(self):
        return self._curragentsloggedin

    @curragentsloggedin.setter
    def curragentsloggedin(self, value):
        self._curragentsloggedin = value
    @property
    def curragenttalking(self):
        return self._curragenttalking

    @curragenttalking.setter
    def curragenttalking(self, value):
        self._curragenttalking = value
    @property
    def currentnotreadyagents(self):
        return self._currentnotreadyagents

    @currentnotreadyagents.setter
    def currentnotreadyagents(self, value):
        self._currentnotreadyagents = value
    @property
    def currentreadyagents(self):
        return self._currentreadyagents

    @currentreadyagents.setter
    def currentreadyagents(self, value):
        self._currentreadyagents = value
    @property
    def currnumberwaitingcalls(self):
        return self._currnumberwaitingcalls

    @currnumberwaitingcalls.setter
    def currnumberwaitingcalls(self, value):
        self._currnumberwaitingcalls = value
    @property
    def endkey(self):
        return self._endkey

    @endkey.setter
    def endkey(self, value):
        self._endkey = value
    @property
    def startkey(self):
        return self._startkey

    @startkey.setter
    def startkey(self, value):
        self._startkey = value
    @property
    def visitorinflow(self):
        return self._visitorinflow

    @visitorinflow.setter
    def visitorinflow(self, value):
        self._visitorinflow = value
    @property
    def visitorresponse(self):
        return self._visitorresponse

    @visitorresponse.setter
    def visitorresponse(self, value):
        self._visitorresponse = value
    @property
    def visitorresponsetransfer(self):
        return self._visitorresponsetransfer

    @visitorresponsetransfer.setter
    def visitorresponsetransfer(self, value):
        self._visitorresponsetransfer = value


    def to_alipay_dict(self):
        params = dict()
        if self.att:
            if hasattr(self.att, 'to_alipay_dict'):
                params['att'] = self.att.to_alipay_dict()
            else:
                params['att'] = self.att
        if self.connectionrate:
            if hasattr(self.connectionrate, 'to_alipay_dict'):
                params['connectionrate'] = self.connectionrate.to_alipay_dict()
            else:
                params['connectionrate'] = self.connectionrate
        if self.curragentsloggedin:
            if hasattr(self.curragentsloggedin, 'to_alipay_dict'):
                params['curragentsloggedin'] = self.curragentsloggedin.to_alipay_dict()
            else:
                params['curragentsloggedin'] = self.curragentsloggedin
        if self.curragenttalking:
            if hasattr(self.curragenttalking, 'to_alipay_dict'):
                params['curragenttalking'] = self.curragenttalking.to_alipay_dict()
            else:
                params['curragenttalking'] = self.curragenttalking
        if self.currentnotreadyagents:
            if hasattr(self.currentnotreadyagents, 'to_alipay_dict'):
                params['currentnotreadyagents'] = self.currentnotreadyagents.to_alipay_dict()
            else:
                params['currentnotreadyagents'] = self.currentnotreadyagents
        if self.currentreadyagents:
            if hasattr(self.currentreadyagents, 'to_alipay_dict'):
                params['currentreadyagents'] = self.currentreadyagents.to_alipay_dict()
            else:
                params['currentreadyagents'] = self.currentreadyagents
        if self.currnumberwaitingcalls:
            if hasattr(self.currnumberwaitingcalls, 'to_alipay_dict'):
                params['currnumberwaitingcalls'] = self.currnumberwaitingcalls.to_alipay_dict()
            else:
                params['currnumberwaitingcalls'] = self.currnumberwaitingcalls
        if self.endkey:
            if hasattr(self.endkey, 'to_alipay_dict'):
                params['endkey'] = self.endkey.to_alipay_dict()
            else:
                params['endkey'] = self.endkey
        if self.startkey:
            if hasattr(self.startkey, 'to_alipay_dict'):
                params['startkey'] = self.startkey.to_alipay_dict()
            else:
                params['startkey'] = self.startkey
        if self.visitorinflow:
            if hasattr(self.visitorinflow, 'to_alipay_dict'):
                params['visitorinflow'] = self.visitorinflow.to_alipay_dict()
            else:
                params['visitorinflow'] = self.visitorinflow
        if self.visitorresponse:
            if hasattr(self.visitorresponse, 'to_alipay_dict'):
                params['visitorresponse'] = self.visitorresponse.to_alipay_dict()
            else:
                params['visitorresponse'] = self.visitorresponse
        if self.visitorresponsetransfer:
            if hasattr(self.visitorresponsetransfer, 'to_alipay_dict'):
                params['visitorresponsetransfer'] = self.visitorresponsetransfer.to_alipay_dict()
            else:
                params['visitorresponsetransfer'] = self.visitorresponsetransfer
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossCsChannelQueryModel()
        if 'att' in d:
            o.att = d['att']
        if 'connectionrate' in d:
            o.connectionrate = d['connectionrate']
        if 'curragentsloggedin' in d:
            o.curragentsloggedin = d['curragentsloggedin']
        if 'curragenttalking' in d:
            o.curragenttalking = d['curragenttalking']
        if 'currentnotreadyagents' in d:
            o.currentnotreadyagents = d['currentnotreadyagents']
        if 'currentreadyagents' in d:
            o.currentreadyagents = d['currentreadyagents']
        if 'currnumberwaitingcalls' in d:
            o.currnumberwaitingcalls = d['currnumberwaitingcalls']
        if 'endkey' in d:
            o.endkey = d['endkey']
        if 'startkey' in d:
            o.startkey = d['startkey']
        if 'visitorinflow' in d:
            o.visitorinflow = d['visitorinflow']
        if 'visitorresponse' in d:
            o.visitorresponse = d['visitorresponse']
        if 'visitorresponsetransfer' in d:
            o.visitorresponsetransfer = d['visitorresponsetransfer']
        return o


