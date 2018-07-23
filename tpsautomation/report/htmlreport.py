#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' generate HTMLReport '''
import os
import tpsautomation.common.constvalue as cv
import tpsautomation.utils.dateandtimeutils as datu


class HTMLReport(object):
    ''' generate HTMLReport '''
    HTML_TMPL = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>%(title)s</title>
            <link href="../css/bootstrap.min.css" rel="stylesheet">
            <h2 style="font-family: Microsoft YaHei;margin-bottom:20px">%(title)s</h2>
            <p class='attribute' style="margin-bottom:10px"><strong>cases路径:</strong> %(casepath)s</p>
            <p class='attribute' style="margin-bottom:10px"><strong>测试结果 : </strong> 共<font color="blue">%(count)s</font>条cases, Pass: <font color="green">%(passed)s</font>, Fail: <font color="red">%(failed)s</font></p>
            <style type="text/css" media="screen">
                body { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
            </style>
        </head>
        <body>
            <table id='result_table' class="table table-bordered table-hover">   
                <tr id='header_row' class="text-center active" style="font-weight: bold;font-size: 14px;">
                    <th width="50px">序号</th>
                    <th width="150px">用例名</th>
                    <th width="110px">用例执行结果</th>
                    <th width="100px">执行时间</th>
                    <th width="100px">执行时长</th>
                    <th>原因</th>
                </tr>
                %(table_tr)s
            </table>
        </body>
        </html>
        """

    TABLE_TMPL = """
        <tr class='%(htmlclass)s'>
            <td>%(id)s</td>
            <td>%(name)s</td>
            <td>%(runresult)s</td>
            <td>%(runtime)s</td>
            <td>%(runduration)s</td>
            <td>%(reason)s</td>
        </tr>
        """

    TABLE_TMPL_NO_CASE = """
        <tr class='active'>
            <td colspan="6">没有找到任何可执行的case</td>
        </tr>
        """

    @staticmethod
    def generete_html_report(result_list, title, path, casepath):
        ''' generete_html_report '''
        table_tr0 = ''
        numfail = 0
        numsucc = 0
        output = ''
        length = len(result_list)
        if length > 0:
            output = HTMLReport.genarete_table(
                result_list, table_tr0, numfail, numsucc, title, casepath)
        else:
            output = HTMLReport.genarete_empty_table(
                result_list, table_tr0, numfail, numsucc, title, casepath)

        name = datu.DateAndTimeUtils.get_today_and_timestamp_as_str_from_timestamp()

        with open(path + os.sep + name + cv.ConstValue.HTML_SUFFIX, 'wb') as file:
            file.write(output.encode('utf-8'))

    @staticmethod
    def genarete_table(result_list, table_tr0, numfail, numsucc, title, casepath):
        ''' genarete_table '''
        for i in result_list:
            table_td = HTMLReport.TABLE_TMPL % i
            table_tr0 += table_td
            if i['runresult'].lower() == cv.ConstValue.CASE_PASS_RESULT:
                numsucc += 1
            elif i['runresult'].lower() == cv.ConstValue.CASE_FAIL_RESULT:
                numfail += 1
        return HTMLReport.genarete_output(len(result_list), table_tr0, numfail, numsucc, title, casepath)

    @staticmethod
    def genarete_empty_table(result_list, table_tr0, numfail, numsucc, title, casepath):
        ''' genarete_empty_table '''
        table_td = HTMLReport.TABLE_TMPL_NO_CASE
        table_tr0 += table_td
        return HTMLReport.genarete_output(len(result_list), table_tr0, numfail, numsucc, title, casepath)

    @staticmethod
    def genarete_output(length, table_tr0, numfail, numsucc, title, casepath):
        ''' genarete_output '''
        output = HTMLReport.HTML_TMPL % dict(
            title=title,
            casepath=casepath,
            count=length,
            passed=numsucc,
            failed=numfail,
            table_tr=table_tr0,
        )
        return output
