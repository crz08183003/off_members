/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2017-08-03 14:33:22
 * @version $Id$
 */
function FnCreateYearMonthDay()
{
   var InputArgArray = FnCreateYearMonthDay.arguments;
   var    selyearname = InputArgArray[0];    //生成下拉列表的id名字(年份)
   var    chosedyear = InputArgArray[1];    //修正值(年份)
   var    selmonthname = InputArgArray[2];    //生成下拉列表的id名字(月份)
   var    chosedmonth = InputArgArray[3];    //修正值(月份)
   var    seldayname = InputArgArray[4];    //生成下拉列表的id名字(日)
   var    chosedday = InputArgArray[5];    //修正值(日)
   
//   var beginyear = InputArgArray[6];    //开始年份(修正值,和当前年份)-10
//   var endyear = InputArgArray[7];        //结束年份(修正值,和当前年份)+5
   
   var argumenetslength = InputArgArray.length;
   
   var outstr = ""; //输出字符串
   var begin_year = 1999;    //开始年
   var today = new Date(); 
   if (argumenetslength==6)
   {
    //复杂类型 //年月日
     //年份
     outstr += '<select id="' + selyearname + '"   name="' + selyearname + '" onchange ="FnResetTrueDate(\'' + selyearname + '\',\'' + selmonthname + '\',\'' + seldayname +'\')" >';
     var todayyear = today.getYear();
     todayyear = todayyear<1900 ? (todayyear+1900):todayyear;
     var End_year=todayyear+10;
//     if(chosedyear!=null&&chosedyear!='')
//     {
//      todayyear += chosedyear;
//     } 
     for (var i=begin_year;i<=End_year;i++)
     { 
      if (i==todayyear)
      {
       outstr = outstr + '<option value="' + i + '" selected=\"selected\">' + i + '年</option>';
      }else{
       outstr = outstr + '<option value="' + i + '">' + i+ '年</option>';
      }
     }
     outstr = outstr + '</select>';
     
     //月份
     outstr = outstr + '<select id="' + selmonthname + '" name="' + selmonthname + '" onchange ="FnResetTrueDate(\'' + selyearname + '\',\'' + selmonthname + '\',\'' + seldayname +'\')" >';
     var todaymonth = today.getMonth() + 1;
     for (i=1;i<=12;i++)
     {
      if (i==todaymonth)
      {
       outstr = outstr + '<option value="' + FnFormatLessTen(i) + '" selected=\"selected\">' + FnFormatLessTen(i) + '月</option>';
      }else{
       outstr = outstr + '<option value="' + FnFormatLessTen(i) + '">' + FnFormatLessTen(i) + '月</option>';
      }
     }
     outstr = outstr + '</select>';
     
     //日期
     outstr += '<select id="' + seldayname + '" name="' + seldayname + '">';
     var todayday = today.getDate();
     var newdate=new Date(todayyear,todaymonth);
     var datenum=newdate.getUTCDate();
     for (i=1;i<=datenum;i++)
     {
      if (i==todayday)
      {
       outstr = outstr + '<option value="' + FnFormatLessTen(i) + '" selected=\"selected\">' + FnFormatLessTen(i) + '日</option>'
      }else{
       outstr = outstr + '<option value="' + FnFormatLessTen(i) + '">' + FnFormatLessTen(i) + '日</option>'
      }
     }
     outstr = outstr + '</select>'
   }
//总输出
   document.write(outstr)
}
function FnFormatLessTen(in_number)
{
   if (in_number<10)
   {
       return("0"+in_number)
   }else{
       return(in_number)
   }
}
function FnResetTrueDate(yearid,monthid,dayid)
{
   var tarobj = document.getElementById(dayid)
   var temp_year=document.getElementById(yearid).value;
   var temp_month=document.getElementById(monthid).value;
   var temp_day=tarobj.value;
   var newdate=new Date(temp_year,temp_month);
   var datenum=newdate.getUTCDate();
   tarobj.length = datenum;
   for(var i=1;i<datenum+1;i++){
       optionday=document.createElement("option");
    optionday.innerHTML = i + "日";
       optionday.setAttribute("value",i);
       tarobj.options[i-1]=optionday;
   }
   if(temp_day<=datenum) 
   tarobj.options[temp_day-1].selected=true;
   else 
      tarobj.options[datenum-1].selected=true;
}
////
//日期生成所用附加函数
//2002-8-19
////
function FnGetSelectValue(obj)
{
   a = document.getElementById(obj)
   return(a.value)
}

  // FnCreateYearMonthDay('my_yeara',0,'my_montha',0,'my_daya',-1)



