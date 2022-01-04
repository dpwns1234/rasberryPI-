//import wait from "waait";
// 전역변수 초기화
var hh = 0;
var mm = 0;
var ss = 0;
var sum_h, sum_m, sum_s;
sum_h = sum_m = sum_s = 0;

//var randomInt = parseInt(Math.random() * 3 + 1); // 1 ~ 3분으로 설정
var randomInt = 15; // 15초로 고정함
var timerId = null;

// 단위 계산
function Calculation(h, m, s, type){
    if(s >= 60)
    {
        m = parseInt(s / 60)
        s = parseInt(s % 60)
    }
    if(m >= 60)
    {
        h = parseInt(m / 60)
        m = parseInt(m % 60)
    }

   document.getElementById(type).innerHTML=h+":"+m+":"+s;

}
function PrintTime() {
    //await wait(1000) // 1초 동안 delay 줘서 연속으로 눌러도 시간이 차지 않게 만들기
    ss++;
    // 5~10 사이의 랜덤 정수와 경과된 시간이 같을 경우 SetRandom()을 부름.
    //if(parseInt(ss/60) == randomInt) 
    if(parseInt(ss) == randomInt) // 15초로 고정함
        SetRandom();
     
    Calculation(hh, mm, ss, "time");
}

function StartClock() {
    //randomInt = parseInt(Math.random() * 3 + 1); // 누적된 randomInt를 초기화
    randomInt = 15; // 실험을 위해 1분으로 고정함
    PrintTime();
    if(timerId == null)
    {
        timerId = setInterval(PrintTime, 1000);
        // 토픽 led로 메서지 On 보내기
        publish('led', 'On');
    }
}

function StopClock() {
    if(timerId != null)
    {
        clearInterval(timerId);
        SumTime();
        // 다 초기값으로 초기화
        hh = mm = ss = 0;
        document.getElementById("time").innerHTML=hh+":"+mm+":"+ss;
        timerId = null;
        // 토픽 led로 메서지 Off 보내기
        publish('led', 'Off');
    }
}

function SumTime() {
    sum_h += hh;
    sum_m += mm;
    sum_s += ss;

    // 단위 계산
    Calculation(sum_h, sum_m, sum_s, "sum_time");
}

// web에서 라즈베리파이의 버튼을 받을 수 있도록 subscribe 해준다.
var isButtonSubscribed = false;
function ButtonOnOff() {
        if(!isButtonSubscribed) {
                subscribe('clock'); // 토픽 clock 등록
                isButtonSubscribed = true;
        }
}

// 5~ 10분 사이에 => random 정수 범위 5~10 설정 후 
// 그것이 if (randomInt == sum_m % 11) { randomPicture(); + randomInt += random}

// randomInt 재설정 후, randomPicture()를 부름.
function SetRandom(){
    // randomInt = randomInt + parseInt(Math.random() * 3 + 1); // 1 ~ 3 중 한 정수 + 그 전에 사진이 찍혔던 시간(=경과된 시간)
    randomInt = 15 // 15초로 고정함
    randomPicture();

}

// 사진을 찍도로 
var isImageSubscribed = false;
function randomPicture() {
        if(!isImageSubscribed) {
                subscribe('image'); // 토픽 image 등록
                isImageSubscribed = true;
        }
        publish('facerecognition', 'action'); // 토픽: facerecognition, action 메시지 전송
}

function ChangeBtn() {
    const btnElement = document.getElementById("timerBtn");

    // 버튼이 눌릴 때마다 이름을 바꿔주고 타이머를 시작한다.
    if(btnElement.value == 'Start')
    {
        StartClock();
        btnElement.value = 'Stop';
    }
    else
    {
        StopClock();
        btnElement.value = 'Start';
    }

}